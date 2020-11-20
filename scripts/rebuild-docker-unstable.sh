# Rebuild docker container
docker rm -f epw-unstable
docker rmi -f epw-unstable
docker build . -t epw-unstable
docker run --name epw-unstable --publish 8001:8080 --restart=always -d --mount source=download-unstable,target=/app/view/static/download epw-unstable
