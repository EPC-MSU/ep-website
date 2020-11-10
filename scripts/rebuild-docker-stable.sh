# Rebuild docker container
docker rm -f epw-stable
docker rmi -f epw-stable
docker build . -t epw-stable
docker run --name epw-stable --publish 8000:8080 --restart=always -d --mount source=download,target=/app/view/static/download epw-stable
