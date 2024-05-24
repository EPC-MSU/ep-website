FROM nginx:bookworm
ENV TZ=Europe/Moscow

RUN apt-get update && \
    apt-get -q -y install apt-utils tzdata git && \
    apt-get -q -y update && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

COPY conf/default.conf /etc/nginx/conf.d/

