# Rebuild docker container
docker rm -f usbadc10-stable
docker rmi -f usbadc10-stable
docker build . -t usbadc10-stable
docker run --name usbadc10-stable --publish 8003:8080 --restart=always -d --mount source=download-usbadc10-stable,target=/app/view/static/download usbadc10-stable
