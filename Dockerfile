FROM python:3.7-slim-buster
ARG SITE_NAME

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y gettext build-essential && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && \
    pip install -r requirements.txt && \
    python minimize.py && \
    cd scripts && ./rebuild-locale.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080
CMD python server.py --debug --site=$SITE_NAME
# docker build --build-arg arg=2.3 .
