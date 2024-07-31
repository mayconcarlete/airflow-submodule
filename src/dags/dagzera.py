from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from datetime import datetime


@dag(
    dag_id="my_first_dag",
    start_date=datetime(2000, 1, 1)
)
def my_dag():
    @task
    def my_task():
        print("My task is being executed")
    my_task()
my_dag()