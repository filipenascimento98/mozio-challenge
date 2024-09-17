FROM python:3.10

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

WORKDIR /usr/src/app
RUN mkdir /var/static/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]