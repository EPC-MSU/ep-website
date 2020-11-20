docker rm -f ep-share-unstable
docker rmi -f ep-share-unstable
docker build dockershare -t ep-share-unstable
docker run --name ep-share-unstable -p 5001:22 -d --restart=always --mount source=download-unstable,target=/drive ep-share-unstable
