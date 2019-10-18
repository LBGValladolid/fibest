FROM python:3.7.5

WORKDIR /opt/fibest

RUN pip install pipenv

COPY Pipfile.lock ./
COPY Pipfile ./
RUN pipenv install --system

COPY . .