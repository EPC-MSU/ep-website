docker rm -f share-stable
docker rmi -f share-stable
docker build dockershare -t share-stable
docker run --name share-stable -p 5000:22 -d --restart=always --mount source=download,target=/drive share-stable
