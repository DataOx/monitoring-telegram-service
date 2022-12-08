FROM python:3.8

RUN apt-get update

RUN pip install --upgrade pip

RUN mkdir /web

WORKDIR /web

COPY web /web

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["bash","/web/entrypoint.sh"]
