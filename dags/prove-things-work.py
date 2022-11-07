from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# from email.policy import default

default_args = {
    "owner": "SB",
    "depends_on_past": False,
    "email": "sribarrow@gmail.com",
    "email_on_failure": "sribarrow@gmail.com",
    "email_on_retry": False,
    "catchup": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
dag = DAG(
    "CreateFile",
    default_args=default_args,
    start_date=datetime(2022, 1, 1, 0, 0),
    schedule_interval=timedelta(minutes=500),
)
task1 = BashOperator(
    task_id="prove_things_work",
    bash_command='echo "hello, world" > /Users/sbmacpro/create-this-file.txt',
    dag=dag,
)
