#! /bin/bash

MONITORING_NAME=""
SCHEDULE_INTERVAL=""

read -p "Enter the monitoringg name: " MONITORING_NAME
read -p "Enter the schedule interval: " SCHEDULE_INTERVAL

echo "logging: Monitoring name: ${MONITORING_NAME} Schedule Interval: ${SCHEDULE_INTERVAL}"
echo "logging: Creating monitoring..."
MONITORING_PATH="/home/maycon/dev/airflow/airflow-submodule/templates"
MONITORING_OUT_DIR="/home/maycon/dev/airflow/airflow-submodule/src/dags"
echo $(python3 -m cookiecutter ${MONITORING_PATH} --no-input monitoring_name="${MONITORING_NAME}" schedule_interval="${SCHEDULE_INTERVAL}" -o ${MONITORING_OUT_DIR})
