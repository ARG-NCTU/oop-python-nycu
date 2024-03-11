#!/usr/bin/env bash

ARGS=("$@")

NAME=rsa
REPOSITORY="argnctu/oop"
TAG="ros-unity"
REPO_NAME=oop-proj-unity-ros

IMG="${REPOSITORY}:${TAG}"


# Make sure processes in the container can connect to the x server
# Necessary so gazebo can create a context for OpenGL rendering (even headless)
XAUTH=/tmp/.docker.xauth
if [ ! -f $XAUTH ]; then
    xauth_list=$(xauth nlist $DISPLAY)
    xauth_list=$(sed -e 's/^..../ffff/' <<<"$xauth_list")
    if [ ! -z "$xauth_list" ]; then
        echo "$xauth_list" | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi

docker run \
    -it \
    --rm \
    -e DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    -e XAUTHORITY=$XAUTH \
    -v "$XAUTH:$XAUTH" \
    -v "/home/$USER/${REPO_NAME}:/home/rsa/${REPO_NAME}" \
    -v "/tmp/.X11-unix:/tmp/.X11-unix" \
    -v "/etc/localtime:/etc/localtime:ro" \
    -v "/dev:/dev" \
    -v "/var/run/docker.sock:/var/run/docker.sock" \
    --user "root:root" \
    --workdir "/home/rsa/${REPO_NAME}" \
    --name "${NAME}" \
    --network host \
    --privileged \
    --security-opt seccomp=unconfined \
    "${IMG}" \
    bash
