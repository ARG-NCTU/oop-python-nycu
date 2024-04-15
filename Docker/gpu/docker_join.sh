#!/usr/bin/env bash
#
# Typical usage: ./join.bash subt
#

BASH_OPTION=bash

IMG=argnctu/oop:gpu

xhost +
containerid=$(docker ps -aqf "ancestor=${IMG}") && echo $containerid
docker exec -it \
    --privileged \
    -e DISPLAY=${DISPLAY} \
    -e LINES="$(tput lines)" \
    ${containerid} \
    $BASH_OPTION
xhost -