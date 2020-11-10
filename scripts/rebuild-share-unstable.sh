docker rm -f share-unstable
docker rmi -f share-unstable
docker build dockershare -t share-unstable
docker run --name share -p 5001:22 -d --restart=always --mount source=download,target=/drive share-unstable
