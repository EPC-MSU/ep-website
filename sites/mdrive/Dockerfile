FROM python:3.7-slim-bookworm

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y gettext build-essential && \
    pip install -r requirements.txt && \
    python minimize.py && \
    msgfmt sites/eyepoint/locale/en_US/LC_MESSAGES/en.po -o sites/eyepoint/locale/en_US/LC_MESSAGES/en.mo --use-fuzzy && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && rm -rf /var/tmp/*

EXPOSE 8080
CMD python server.py --site=mdrive
