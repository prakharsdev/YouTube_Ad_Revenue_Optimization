from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from notifications.telegram_bot import (
    notify_pipeline_start, 
    notify_pipeline_success, 
    notify_pipeline_failure,
    notify_model_training_completion,
    notify_ad_revenue_prediction
)

def fetch_and_upload():
    try:
        from data_ingestion.upload_to_s3 import upload_to_s3
        from data_ingestion.fetch_youtube_data import fetch_youtube_data
        data = fetch_youtube_data()
        upload_to_s3(data, 'raw/youtube_data.json')
        notify_pipeline_success()
    except Exception as e:
        notify_pipeline_failure(str(e))
        raise

def process_data():
    from data_processing.process_data import spark
    try:
        # Processing logic goes here
        spark.stop()
        notify_pipeline_success()
    except Exception as e:
        notify_pipeline_failure(str(e))
        raise

def train_model():
    try:
        from ml_model.train_model import train_model
        train_model()
        notify_model_training_completion()
        notify_pipeline_success()
    except Exception as e:
        notify_pipeline_failure(str(e))
        raise

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 1),
    'retries': 1,
}

dag = DAG('youtube_data_pipeline', default_args=default_args, schedule_interval='@daily')

start = DummyOperator(task_id='start', dag=dag)
notify_start = PythonOperator(task_id='notify_start', python_callable=notify_pipeline_start, dag=dag)

fetch_upload = PythonOperator(task_id='fetch_and_upload', python_callable=fetch_and_upload, dag=dag)
process = PythonOperator(task_id='process_data', python_callable=process_data, dag=dag)
train = PythonOperator(task_id='train_model', python_callable=train_model, dag=dag)

start >> notify_start >> fetch_upload >> process >> train
