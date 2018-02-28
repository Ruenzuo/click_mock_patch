FROM python:2.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt requirements-tests.txt ./
RUN pip install --no-cache-dir -r requirements-tests.txt
