FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y gettext build-essential

RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN pip install -r requirements.txt

RUN python minimize.py && \
    msgfmt sites/eyepoint/locale/en_US/LC_MESSAGES/en.po -o sites/eyepoint/locale/en_US/LC_MESSAGES/en.mo --use-fuzzy

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080
CMD python server.py --site=eyepoint
