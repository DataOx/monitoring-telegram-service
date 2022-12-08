FROM python:3.8

RUN apt-get update

RUN pip install --upgrade pip

RUN mkdir /bot

WORKDIR /bot

COPY services /bot

RUN pip install -r requirements.txt

CMD python bot.py
