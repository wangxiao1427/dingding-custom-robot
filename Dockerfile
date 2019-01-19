FROM agoradigital/python3.7-pandas-psycopg2-alpine
# FROM python:3.7-alpine
MAINTAINER wangxiao <wang.xiao@intellif.com>

ENV FLASK_APP run.py
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "6799"]