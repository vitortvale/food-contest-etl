from contestapi import generate_order
from airflow.models.dag import DAG #type: ignore
from airflow.operators.python import PythonOperator                                             # type: ignore
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator            # type: ignore
from datetime import datetime

dag = DAG(
    dag_display_name="BurgerContest",
    dag_id = "process_sales",
    schedule = "None",
    start_date = datetime(2024,1,1)
)

create_or_get_db = SQLExecuteQueryOperator(                                                # type: ignore
    task_id = "create_or_get_db",
    sql = "sql/order_schema.sql",
    dag = dag
)

insert_trucks = SQLExecuteQueryOperator(                                                    # type: ignore
    task_id="insert_trucks",
    sql = "sql/insert_trucks.sql",
    dag = dag
)

insert_burgers = SQLExecuteQueryOperator(                                                    # type: ignore
    task_id = "insert_burgers",
    sql = "sql/insert_burgers.sql",
    dag = dag
)

#get_order_from_api = PythonOperator(
#    task_id = "get_order",
#    python_callabe = generate_order,
#    dag = dag
#)

create_or_get_db >> insert_trucks >> insert_burgers



