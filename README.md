# airflow
pip install virtualenv
virtualenv --python=python3 venv

virtualenv venv
source venv/bin/activate

pip3 install apache-airflow

pip3 install apache-airflow[psycopg2]

pip3 install apache-airflow[rabbitmq]

pip3 install apache-airflow[celery]

(venv) $ cd /path/to/my/airflow
(venv) $ export AIRFLOW_HOME=`pwd`/airflow_home

#initilize DB
(venv) $ airflow initdb
#run server
airflow webserver

# To run dag
cd /path/to/my/airflow/airflow_home
$ export AIRFLOW_HOME=`pwd`/airflow_home
$ source venv/bin/activate
#run scheduler
(venv) $ airflow scheduler

