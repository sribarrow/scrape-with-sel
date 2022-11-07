from datetime import date
from datetime import datetime

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {"mysql_conn_id": "airflow_db"}

with DAG(
    "first_etl_dag",
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    # extracting data
    extract_file = "/Users/sbmacpro/airflow_demo/raw/airflow-extract-data.csv"

    print(f"Extracting data to {extract_file}")
    extract_task = BashOperator(
        task_id="extract-task",
        bash_command="wget -c "
        "https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O "
        + extract_file,
    )
    extract_task

    # trasforming data
    def transform_data():
        """
        Read in the extract and output transformed
        data to a file
        """
        transform_file = (
            "/Users/sbmacpro/airflow_demo/transformed/airflow-transformed-data.csv"
        )
        df = pd.read_csv(extract_file)
        print(f"Number of rows before transformation: {len(df)}")
        generic_type_df = df[df["Type"] == "generic"]
        generic_type_df["Date"] = today.strftime("%Y-%m-%d")
        print(f"Processing date: {today}. Writing data to {transform_file}")
        generic_type_df.to_csv(transform_file, index=False)
        print(f"Number of rows after transformation: {len(generic_type_df)}")

    today = date.today()
    print(f"Processing date: {today}. Reading data from {extract_file}")
    transform_task = PythonOperator(
        task_id="transform_task", python_callable=transform_data, dag=dag
    )
    transform_task

    print("Extracting data to Database")

    load_to_db_task = MySqlOperator(
        task_id="load_to_db_task",
        sql=r"""
        USE airflow_db;
        LOAD DATA INFILE '/Users/sbmacpro/airflow_demo/transformed/airflow-transformed-data.csv'
        INTO TABLE top_level_domains
        FIELDS TERMINATED BY ',' ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES;
        """,
        dag=dag,
    )
    load_to_db_task
    # transform_data()
    extract_task >> transform_task >> load_to_db_task
