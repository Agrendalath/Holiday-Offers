FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN groupadd -r api && \
    useradd -mr -g api api

RUN pip install pipenv && \
    mkdir /app

COPY ./compose/production/api/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

USER api
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
WORKDIR /app

RUN pipenv sync

COPY ./holiday_offers /app/holiday_offers

USER root
RUN chown -R api:api /app

USER api
