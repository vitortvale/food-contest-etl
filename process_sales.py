from contestapi import generate_order
from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore


dag = DAG(
    dag_id = "process_sales",
    schedule = "* * * * *"
)

fetch_from_api_task = PythonOperator(
    task_id = "fetch_from_api",
    python_callable = generate_order,
    dag = dag
)


