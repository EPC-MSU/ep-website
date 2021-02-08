# Rebuild docker container
docker rm -f usbadc10-unstable
docker rmi -f usbadc10-unstable
docker build . -t usbadc10-unstable
docker run --name usbadc10-unstable --publish 8002:8080 --restart=always -d --mount source=download-usbadc10-unstable,target=/app/view/static/download usbadc10-unstable
