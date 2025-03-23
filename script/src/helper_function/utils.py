import os
import json
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pyspark.sql.functions import col, count, when, round

# Load .env and define the credentials
load_dotenv("/home/jovyan/work/.env", override=True)

SOURCE_DB_HOST = os.getenv("SOURCE_DB_HOST")
SOURCE_DB_NAME = os.getenv("SOURCE_DB_NAME")
SOURCE_DB_USER = os.getenv("SOURCE_DB_USER")
SOURCE_DB_PASS = os.getenv("SOURCE_DB_PASS")
SOURCE_DB_PORT = os.getenv("SOURCE_DB_PORT")

DWH_DB_HOST = os.getenv("DWH_DB_HOST")
DWH_DB_NAME = os.getenv("DWH_DB_NAME")
DWH_DB_USER = os.getenv("DWH_DB_USER")
DWH_DB_PASS = os.getenv("DWH_DB_PASS")
DWH_DB_PORT = os.getenv("DWH_DB_PORT")

LOG_DB_HOST = os.getenv("LOG_DB_HOST")
LOG_DB_NAME = os.getenv("LOG_DB_NAME")
LOG_DB_USER = os.getenv("LOG_DB_USER")
LOG_DB_PASS = os.getenv("LOG_DB_PASS")
LOG_DB_PORT = os.getenv("LOG_DB_PORT")


def source_engine():
    SOURCE_DB_URL = f"jdbc:postgresql://{SOURCE_DB_HOST}:{SOURCE_DB_PORT}/{SOURCE_DB_NAME}"
    return SOURCE_DB_URL, SOURCE_DB_USER, SOURCE_DB_PASS 

def dwh_engine():
    DWH_DB_URL = f"jdbc:postgresql://{DWH_DB_HOST}:{DWH_DB_PORT}/{DWH_DB_NAME}"
    return DWH_DB_URL, DWH_DB_USER, DWH_DB_PASS 

def dwh_engine_sqlalchemy():
    return create_engine(f"postgresql://{DWH_DB_USER}:{DWH_DB_PASS}@{DWH_DB_HOST}:{DWH_DB_PORT}/{DWH_DB_NAME}")

def log_engine():
    LOG_DB_URL = f"jdbc:postgresql://{LOG_DB_HOST}:{LOG_DB_PORT}/{LOG_DB_NAME}"
    return LOG_DB_URL, LOG_DB_USER, LOG_DB_PASS 


def load_log_msg(spark: SparkSession, log_msg):

    LOG_DB_URL, LOG_DB_USER, LOG_DB_PASS = log_engine()
    table_name = "etl_log"

    # set config
    connection_properties = {
        "user": LOG_DB_USER,
        "password": LOG_DB_PASS,
        "driver": "org.postgresql.Driver" # set driver postgres
    }

    log_msg.write.jdbc(url = LOG_DB_URL,
                  table = table_name,
                  mode = "append",
                  properties = connection_properties)



# Create a function to save the final report to a JSON file
def save_to_json(dict_result: dict, filename: str) -> None:
    """
    This function saves the data profiling result to a JSON file.

    Args:
        dict_result (dict): Data profiling result to save to a JSON file.
        filename (str): Name of the JSON file to save the data profiling result to.

    Returns:
        None
    """

    try:
        
        # Save the data profiling result to a JSON file
        with open(f'{filename}.json', 'w') as file:
            file.write(json.dumps(dict_result, indent= 4))
    
    except Exception as e:
        print(f"Error: {e}")



# Check Percentage of Missing Values for each column with pyspark
def check_missing_values(df):

    total_data = df.count()

    # Calculate the percentage of missing values for each column
    get_missing_values = df.select([
        round((count(when(col(c).isNull(), c)) / total_data) * 100, 2).alias(c)
        for c in df.columns
    ]).collect()[0].asDict()
    
    return get_missing_values
