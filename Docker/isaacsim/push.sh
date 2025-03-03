#!/usr/bin/env bash

REPOSITORY="argnctu/oop"
TAG="isaacsim"

IMG="${REPOSITORY}:${TAG}"

docker image push "${IMG}"
