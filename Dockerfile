FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update && \
    apt-get install -y gettext build-essential && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
RUN pip install -r requirements.txt && \
    python minimize.py && \
    msgfmt locale/en_US/LC_MESSAGES/en.po -o locale/en_US/LC_MESSAGES/en.mo --use-fuzzy

EXPOSE 8080
EXPOSE 8443
cmd ["python", "server.py"]
