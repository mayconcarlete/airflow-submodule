from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "maycon.carlete@gmail.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def print_hello():
    print("Your Dag is working as expected!")


with DAG(
        dag_id="test_dag_example",
        start_date=datetime(2021, 1, 1),
        schedule_interval="@daily",
        default_args=default_args,
        catchup=False
    ) as dag:
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )