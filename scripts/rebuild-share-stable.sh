docker rm -f usbadc10-share-stable
docker rmi -f usbadc10-share-stable
docker build dockershare -t usbadc10-share-stable
docker run --name usbadc10-share-stable -p 5003:22 -d --restart=always --mount source=download-usbadc10-stable,target=/drive usbadc10-share-stable
