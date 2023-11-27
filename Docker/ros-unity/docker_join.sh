#!/usr/bin/env bash

NAME=aoop
REPOSITORY="argnctu/ros-unity"
TAG="latest"
REPO_NAME=oop-proj-unity-ros

IMG="${REPOSITORY}:${TAG}"

xhost +
containerid=$(docker ps -aqf "ancestor=${IMG}") && echo "$containerid"
docker exec -it \
    --privileged \
    -e DISPLAY="${DISPLAY}" \
    -e LINES="$(tput lines)" \
    "${containerid}" \
    bash
xhost -
