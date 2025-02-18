from contestapi import generate_order
from airflow import DAG
from airflow.operators.python import PythonOperator                                             # type: ignore
from airflow.operators.postgres_operator import SQLExecuteQueryOperator #maybe wrong            # type: ignore

dag = DAG(
    dag_id = "process_sales",
    schedule = "once"
)




