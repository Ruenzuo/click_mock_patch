#!/usr/bin/env bash

docker build -t click-mock-patch .
docker run -v $PWD:/usr/src/app click-mock-patch:latest nosetests -v tests
