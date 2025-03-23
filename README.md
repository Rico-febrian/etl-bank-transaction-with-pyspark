# **End-to-end ETL Pipeline with PySpark**

## Overview

Hello, welcome to my learning logs!

In this project, I share how I developed an **ETL (Extract, Transform, Load) pipeline** using **PySpark** with a dataset related to bank transactions. The goal is to build a complete ETL pipeline and automate the process efficiently based on a real-world case.


## Problem Statement

- The data is **scattered across multiple sources**, making integration complex.
- The dataset is **large**, requiring optimized computational resources.
- Raw data is **unstructured**, making it unsuitable for direct analysis.


## Data Sources

The data comes from two primary sources:

1. **Database**
   - Stores information on phone-based direct marketing campaigns conducted by a bank to promote a **term deposit product**.
   - Includes the following tables:
     - `education_status`
     - `marital_status`
     - `marketing_campaign_deposit`

2. **CSV File**
   - Contains transactional and demographic data for over **800,000 banking customers**.
   - Provides details such as **account balances** and **transaction history**.


## Solution Approach

Assume I have already conducted requirement gathering, and the agreed solution was to **develop an ETL pipeline using PySpark** to streamline data extraction, transformation, and loading into the data warehouse

## Pipeline Design

![pipeline_design](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/assets/etl_with_pyspark_design.png)

## Development Process

Here’s a brief summary of the steps I took to develop the ETL pipeline:

1. Set Up PySpark and Database
   - Set up PySpark in Jupyter Notebook and configured the necessary databases, including the source database, data warehouse, and log database. I used [Docker Compose](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/docker-compose.yml) for this setup.

2. Create Helper Functions
   - Created functions to support the ETL pipeline, such as setting up the database engine and other utilities.

3. **Extract Data**
   - Created functions to extract data from both **databases** and **CSV files**.

4. **Data Profiling**
   - Analyzed the data structure and generated [**profiling reports**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/script/data_profiling_report.json) stored in **JSON format**.

5. **Source-to-Target Mapping**
   - Defined transformation rules to keep the data accurate and consistent. Assume these mappings were gathered during the requirements gathering with user.

6. **Data Transformation**
   - Applied transformation functions for each table based on [**source-to-target mapping**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/source-to-target-map.md).

7. **Load Data**
   - Created functions to load transformed data into the **data warehouse**.

8. **Create Pipeline and Automation**
   - I Developed and tested functions in **Jupyter Notebook**, then organized the pipeline into structured modules, such as:

     - [**Helper functions**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/tree/main/script/src/helper_function)
     - [**Extract module**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/tree/main/script/src/extract)
     - [**Profiling module**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/tree/main/script/src/profiling)
     - [**Transform module**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/tree/main/script/src/transform)
     - [**Load module**](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/tree/main/script/src/load)
       
   
   - Then finally, I created a main script to run these modules and automated the execution.

## How to Run the ETL Pipeline

1. **Set up the environment** (Ensure PySpark is installed).

2. **Run the main script**:
   
   ```
   python main.py
   ```
3. **Monitor logs** to validate the execution and detect potential issues.

## Result

- ETL log result in log database

![etl_log](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/assets/etl_log_result.png)

- Main pipeline result

![main_pipeline](https://github.com/Rico-febrian/etl-bank-transaction-with-pyspark/blob/main/assets/main_pipeline_result.png)

## Final Thoughts

That’s it! I hope this sharing is helpful for anyone learning about this too.

I’d love to hear your feedback and thoughts! I also share my learning journey on **Medium**, so feel free to check it out [here](https://medium.com/@ricofebrian731). You can also connect with me on LinkedIn [here](www.linkedin.com/in/ricofebrian).

Thank you!