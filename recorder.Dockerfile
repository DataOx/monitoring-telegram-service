FROM python:3.8

RUN apt-get update

RUN pip install --upgrade pip

RUN mkdir /recorder

WORKDIR /recorder

COPY services /recorder

RUN pip install -r requirements.txt

CMD python recorder.py
