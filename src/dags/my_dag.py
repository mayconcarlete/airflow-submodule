import datetime
from airflow.sdk import DAG
import random
from airflow.providers.standard.operators.python import PythonOperator

def data() -> dict:
    number = random.randint(1, 10)
    return {
        "number": number
    }

def data_task(ti):
    number = data()
    # push to Minio and XCOM the path
    ti.xcom_push(key='data', value=number)


def process(path: str)->None:
    print("Data value")
    # print(data)

def process_task(ti):
    # Receives the PATH via XCOM 
    path = ti.xcom_pull(task_ids="get_dats", key='data')
    
    process(data)
    print("Processing Data")

with DAG(
    dag_id="My_first_dag",
    tags="Fraud",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily"
):
    get_data=PythonOperator(
        python_callable=data_task,
        task_id="get_dats"
    )

    process_data=PythonOperator(
        python_callable=process_task,
        task_id="process_dats"
    )

    get_data >> process_data