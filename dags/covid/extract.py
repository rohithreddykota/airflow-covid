from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from covid.utils import get_covid_data, json_to_df, load_to_stage_area
import json

DEFAULT_ARGS = {
    'owner': 'extractor',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime(2020,12,23),
    'schedule_interval': '@daily'
}

DAG_ID = 'covid'

with DAG(dag_id=DAG_ID, default_args=DEFAULT_ARGS) as dag:
    with open('/usr/local/airflow/dags/covid/sqls/ddl_covid_timeseries.sql', 'r') as f:
        sql = f.read()
    create_table_if_not_exists = PostgresOperator(task_id='check_table', postgres_conn_id='staging' ,sql=sql)

    extract = PythonOperator(
        task_id='extract',
        python_callable=get_covid_data,
        op_kwargs={'uri':'https://api.covid19india.org/v4/timeseries.json'},
        provide_context=True
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=json_to_df,
        op_kwargs={'start_date': '2020-01-01', 
                'end_date': '9999-12-31'},
        provide_context=True
    )

    stage_load = PythonOperator(
        task_id='stage_load',
        python_callable=load_to_stage_area,
        provide_context=True
    )

    with open('/usr/local/airflow/dags/covid/sqls/target_load.sql', 'r') as f:
        sql = f.read()
    target_load = PostgresOperator(task_id='target_load', postgres_conn_id='staging', sql=sql)

    create_table_if_not_exists >> stage_load
    extract >> transform >> stage_load >> target_load