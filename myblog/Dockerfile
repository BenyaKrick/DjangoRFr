FROM python:3.10.6

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8001
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
