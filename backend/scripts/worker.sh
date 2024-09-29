#!/bin/bash

echo "RabbitMQ Connection --- Establishing . . ."

while ! nc -z $RABBIT_HOST $RABBIT_PORT; do
    sleep 1
    echo "Waiting for RabbitMQ --- Retrying . . ."
done

echo "RabbitMQ Connection --- Successfully Established!"
echo "FastStream Application --- Running . . ."

python -m src.bidhub.main.worker
