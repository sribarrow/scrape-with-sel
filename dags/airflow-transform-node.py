from datetime import date
from datetime import datetime

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="transform_dag",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:

    def transform_data():
        """
        Read in the extract and output transformed
        data to a file
        """
        today = date.today()
        print(f"Processing date: {today}")
        df = pd.read_csv("/Users/sbmacpro/airflow_demo/raw/airflow-extract-data.csv")
        print(f"Number of rows before transformation: {len(df)}")
        generic_type_df = df[df["Type"] == "generic"]
        generic_type_df["Date"] = today.strftime("%Y-%m-%d")
        generic_type_df.to_csv(
            "/Users/sbmacpro/airflow_demo/transformed/airflow-transformed-data.csv",
            index=False,
        )
        print(f"Number of rows after transformation: {len(generic_type_df)}")
        transform_task = PythonOperator(
            task_id="transform_task", python_callable=transform_data, dag=dag
        )

        transform_task
