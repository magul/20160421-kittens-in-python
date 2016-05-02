#! /bin/bash

docker build -t kittens .
docker run -ti -p 8000:80 kittens
