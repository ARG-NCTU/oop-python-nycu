#!/usr/bin/env bash

REPOSITORY="argnctu/oop"
TAG="isaacsim"

IMG="${REPOSITORY}:${TAG}"

docker pull "${IMG}"
