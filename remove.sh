docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi ao:metal.v0
