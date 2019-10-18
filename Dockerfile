FROM python:3.8.0

WORKDIR /opt/fibest

RUN pip install pipenv

COPY Pipfile.lock ./
COPY Pipfile ./
RUN pipenv install --system

COPY . .