FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN groupadd -r api && \
    useradd -mr -g api api

RUN pip install pipenv && \
    mkdir /app

COPY ./compose/local/api/start.sh /start.sh
COPY ./compose/local/api/test.sh /app/test.sh
RUN sed -i 's/\r//' /start.sh && \
    sed -i 's/\r//' /app/test.sh
RUN chmod +x /start.sh /app/test.sh

USER api
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
WORKDIR /app

RUN pipenv sync --dev

COPY . /app

USER root
RUN chown -R api:api /app

USER api
