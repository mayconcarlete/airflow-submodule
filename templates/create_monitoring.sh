#! /bin/bash

MONITORING_NAME=""
SCHEDULE_INTERVAL=""
START_DATE=""


# get the data from using these questions
read -p "Enter the monitoringg name: " MONITORING_NAME
read -p "Enter the schedule interval: " SCHEDULE_INTERVAL
read -p "Enter the start date: " START_DATE

# logging
echo "logging: Monitoring name: ${MONITORING_NAME} Schedule Interval: ${SCHEDULE_INTERVAL} start date: ${START_DATE}"
echo "logging: Creating monitoring..."

MONITORING_PATH="/home/maycon/dev/airflow/airflow-submodule/templates"
MONITORING_OUT_DIR="/home/maycon/dev/airflow/airflow-submodule/src/dags"

echo $(python3 -m cookiecutter ${MONITORING_PATH} --no-input monitoring_name="${MONITORING_NAME}" schedule_interval="${SCHEDULE_INTERVAL} date" -o ${MONITORING_OUT_DIR})
