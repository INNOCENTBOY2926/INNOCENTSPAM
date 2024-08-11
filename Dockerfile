FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip install telethon
RUN pip install cryptg
RUN pip install heroku3
CMD python3 main.py

