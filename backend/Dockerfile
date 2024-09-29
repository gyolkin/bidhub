# RABBIT STAGE
FROM rabbitmq:3.13-management-alpine as rabbit-stage

RUN apk add --no-cache curl

ENV DELAYED_PLUGIN_VERSION=3.13.0

RUN curl -L -o /plugins/rabbitmq_delayed_message_exchange-${DELAYED_PLUGIN_VERSION}.ez \
    https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/releases/download/v${DELAYED_PLUGIN_VERSION}/rabbitmq_delayed_message_exchange-${DELAYED_PLUGIN_VERSION}.ez

RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange

# PYTHON REQUIREMENTS
FROM python:3.10-slim as requirements-stage

WORKDIR /tmp

RUN pip install --upgrade pip &&\
    pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# BASE STAGE
FROM python:3.10-slim as base-stage

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir --upgrade -r requirements.txt

RUN apt-get update \
    && apt-get -y install netcat-traditional \
    && apt-get clean

# WEB API STAGE
FROM base-stage as web-api-stage

COPY /scripts/web_api.sh /app/entry.sh
RUN chmod +x /app/entry.sh

COPY alembic.ini /app/alembic.ini
COPY /src /app/src

ENV PYTHONPATH /app/src:$PYTHONPATH
ENTRYPOINT ["/app/entry.sh"]

# WORKER STAGE
FROM base-stage as worker-stage

COPY /scripts/worker.sh /app/entry.sh
RUN chmod +x /app/entry.sh

COPY alembic.ini /app/alembic.ini
COPY /src /app/src

ENV PYTHONPATH /app/src:$PYTHONPATH
ENTRYPOINT ["/app/entry.sh"]
