FROM python:3.10.0-alpine3.14

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev
RUN pip install --upgrade cython

RUN pip install --upgrade pip


COPY ./requirements.txt \requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /django
COPY . . 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

