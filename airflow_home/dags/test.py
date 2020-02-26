import time
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello(**kwargs):
    time.sleep(10)
    return 'Hello world!' + kwargs['key1']

def print_hello_start(**kwargs):
    return 'Hello world! start task'  + kwargs['key1']

dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='* * * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_hello_start,
    dag=dag,
)

#dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
dummy_operator_end = DummyOperator(task_id='end_dummy_task', retries=3, dag=dag)
# parallel_run = 10
# for i in range(10):
#     data = str(i)
#     hello_operator = PythonOperator(
#         task_id='hello_task', python_callable=print_hello,op_kwargs={'key1': data}, dag=dag
#     )
#     dummy_operator >> hello_operator

for i in range(5):
    data = str(i)
    task = PythonOperator(

        task_id='sleep_for_' + str(i),
        python_callable=print_hello,
        op_kwargs={'key1': data},
        dag=dag,
    )

    run_this >> task

task >> dummy_operator_end



#dummy_operator >> hello_operator >> dummy_operator_end

#dummy_operator >> hello_operator >> dummy_operator_end