FROM python:3.7-alpine

WORKDIR /opt/covid-exporter

COPY src/Pipfile .
COPY src/Pipfile.lock .

RUN pip install pipenv

RUN pipenv install 

COPY src/__main__.py /opt/covid-exporter/
COPY src/src /opt/covid-exporter/src

