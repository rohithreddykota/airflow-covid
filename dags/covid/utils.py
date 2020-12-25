import requests
import pandas as pd
from sqlalchemy import create_engine
from airflow.hooks.base_hook import BaseHook
import json

TABLE_NAME = 'temp_covid_time_series'

def json_to_df(start_date, end_date, **context):
    '''
    takes covid json and return convert into json
    '''
    covid_data = json.loads(context['ti'].xcom_pull(task_ids="extract"))
    cleansed = []
    for state, state_metrics in covid_data.items():
        for date, metrics in state_metrics.get('dates').items():
            if date >= start_date and date < end_date:
                for metric_type, metric_attr in metrics.items():
                        cleansed.append(dict(state=state,
                            date_value=date,
                            metric_type=metric_type,
                            **metric_attr
                            ))
    return pd.DataFrame(cleansed)

def get_covid_data(**context):
    return json.dumps(requests.get(context['uri']).json())

def load_to_stage_area(**context):
    df = context['ti'].xcom_pull(task_ids="transform")
    engine = create_engine('postgresql://staging:staging@staging:5432/staging')
    df.to_sql(TABLE_NAME, engine)