FROM python:3.8.5

RUN pip install --upgrade pip

RUN mkdir /app_grupo3
WORKDIR /app_grupo3

COPY . /app_grupo3

RUN pip install -r requirements.txt

ENV EN_DOCKER=True

RUN mkdir /data

CMD ["python" , "tp_iw/manage.py" , "runserver" , "0.0.0.0:8000"]

#CMD ["sh", "-c", "/app_grupo3/start.sh"]