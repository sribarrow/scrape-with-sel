from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "extract_dag",
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:
    extract_task = BashOperator(
        task_id="extract-task",
        bash_command="wget -c "
        "https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv "
        "-O /Users/sbmacpro/airflow_demo/raw/airflow-extract-data.csv",
    )
    extract_task
