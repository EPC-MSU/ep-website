docker rm -f usbadc10-share-unstable
docker rmi -f usbadc10-share-unstable
docker build dockershare -t usbadc10-share-unstable
docker run --name usbadc10-share-unstable -p 5002:22 -d --restart=always --mount source=download-usbadc10-unstable,target=/drive usbadc10-share-unstable
