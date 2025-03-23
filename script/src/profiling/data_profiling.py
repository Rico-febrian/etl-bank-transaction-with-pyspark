import pyspark
from pyspark.sql import SparkSession
from datetime import datetime
from src.helper_function.utils import check_missing_values, save_to_json
from src.extract.extract_data import extract_database, extract_csv


# Create SparkSession
spark = SparkSession.builder \
    .appName("Data Profiling") \
    .getOrCreate()

# Extract data
education_status_df = extract_database(spark=spark, table_name="education_status")
marital_status_df = extract_database(spark=spark, table_name="marital_status")
marketing_campaign_deposit_df = extract_database(spark=spark, table_name="marketing_campaign_deposit")
bank_df = extract_csv(spark=spark, file_name="new_bank_transaction.csv")

# Create data profiling report
data_profiling_report = {
    "person_in_charge" : "rico_febrian",
    "checking_date" : datetime.now().strftime('%d/%m/%y'),
    "Column Information": {
        "Education Status": {"count": len(education_status_df.columns), "columns": education_status_df.columns},
        "Marital Status": {"count": len(marital_status_df.columns), "columns": marital_status_df.columns},
        "Marketing Campaign Deposit": {"count": len(marketing_campaign_deposit_df.columns), "columns": marketing_campaign_deposit_df.columns},
        "Bank Transaction": {"count": len(bank_df.columns), "columns": bank_df.columns},
    },
    "Check Data Size": {
        "Education Status": education_status_df.count(),
        "Marital Status": marital_status_df.count(),
        "Marketing Campaign Deposit": marketing_campaign_deposit_df.count(),
        "Bank Transaction": bank_df.count(),
    },
    "Data Type For Each Column" : {
        "education status": education_status_df.dtypes,
        "marital status": marital_status_df.dtypes,
        "marketing campaign deposit": marketing_campaign_deposit_df.dtypes,
        "bank transaction": bank_df.dtypes
    },
    "Check Missing Value" : {
        "education status": check_missing_values(education_status_df),
        "marital status": check_missing_values(marital_status_df),
        "marketing campaign deposit": check_missing_values(marketing_campaign_deposit_df),
        "bank transaction": check_missing_values(bank_df)
    }
}

# Save data profiling report to json
save_to_json(dict_result=data_profiling_report, filename="data_profiling_report")

