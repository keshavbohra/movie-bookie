FROM python:3.7

LABEL maintainer="Keshav Bohra <keshav.bohra@gmail.com>"

COPY . /booking_app
WORKDIR /booking_app

RUN pip install -r requirements.txt
