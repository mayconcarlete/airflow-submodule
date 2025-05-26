#/bin/bash

USER=$(id -u) GID=$(id -g)  

docker compose -f docker-compose.yaml -f minio-compose.yaml up -d

