FROM python:3.8.5

RUN mkdir /app_grupo3
WORKDIR /app_grupo3

COPY . /app_grupo3

RUN pip install -r requirements.txt

ENV EN_DOCKER=True

RUN mkdir /data
COPY tp_iw/db.sqlite3 /../data

CMD ["sh", "-c", "/app_grupo3/start.sh"]