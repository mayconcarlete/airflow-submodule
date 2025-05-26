#/bin/bash

docker compose up airflow-init
sudo chown -R ${USER}:${USER} -R src airflow