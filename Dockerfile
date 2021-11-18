FROM python:3.10.0-alpine3.14

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt \requirements.txt
RUN pip install -r /requirements.txt


WORKDIR /app
COPY . . 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

