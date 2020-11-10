docker rm -f ep-share-unstable
docker rmi -f ep-share-unstable
docker build dockershare -t share-unstable
docker run --name share -p 5001:22 -d --restart=always --mount source=download-unstable,target=/drive share-unstable
