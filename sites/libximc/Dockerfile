FROM nginx:bookworm
ENV TZ=Europe/Moscow

RUN apt-get update && \
    apt-get -q -y install apt-utils tzdata git && \
    apt-get -q -y update && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    sed -i 's/access_log\  \/var\/log\/nginx\/access\.log\  main\;/map $status $loggable {\n        ~^[404\]  0;\n        default 1;\n    }\n\n    access_log\  \/var\/log\/nginx\/access\.log\  main\ if\=\$loggable\;\n\n    log_not_found off;/1' /etc/nginx/nginx.conf && \
    sed -i 's/usr\/share\/nginx\/html/var\/www\/html/1' /etc/nginx/conf.d/default.conf && \
    sed -i 's/index\  index\.html\ index\.htm;/index\    index\.html;\n        autoindex on;\n        autoindex_exact_size off;\n        autoindex_localtime on;\n/1' /etc/nginx/conf.d/default.conf

