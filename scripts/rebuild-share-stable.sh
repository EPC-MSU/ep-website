docker rm -f ep-share-stable
docker rmi -f ep-share-stable
docker build dockershare -t ep-share-stable
docker run --name ep-share-stable -p 5000:22 -d --restart=always --mount source=download,target=/drive ep-share-stable
