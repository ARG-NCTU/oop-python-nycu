#!/usr/bin/env bash

ARGS=("$@")

REPOSITORY="argnctu/oop"
TAG="isaacsim"

IMG="${REPOSITORY}:${TAG}"

USER_NAME="arg"
REPO_NAME="oop-python-nycu"
CONTAINER_NAME="isaacsim"

CONTAINER_ID=$(docker ps -aqf "ancestor=${IMG}")
if [ $CONTAINER_ID ]; then
  echo "Attach to docker container $CONTAINER_ID"
  xhost +
  docker exec --privileged -e DISPLAY=${DISPLAY} -e LINES="$(tput lines)" -it ${CONTAINER_ID} bash
  xhost -
  return
fi

# Make sure processes in the container can connect to the x server
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

# Prevent executing "docker run" when xauth failed.
if [ ! -f $XAUTH ]; then
  echo "[$XAUTH] was not properly created. Exiting..."
  exit 1
fi


docker run --workdir "/home/${USER_NAME}/${REPO_NAME}" \
    -it \
    --rm \
    --gpus all \
    --privileged \
    --network=host \
    --runtime=nvidia \
    --entrypoint bash \
    --name "${CONTAINER_NAME}" \
    --security-opt seccomp=unconfined \
    -e "ACCEPT_EULA=Y" \
    -e USER=${USER_NAME} \
    -e XAUTHORITY=$XAUTH \
    -e HOME=/home/${USER_NAME} \
    -e NVIDIA_DRIVER_CAPABILITIES=all \
    -e OPENAI_API_KEY=${OPENAI_API_KEY} \
    -v "/dev:/dev" \
    -v "$XAUTH:$XAUTH" \
    -v "/var/run/docker.sock:/var/run/docker.sock" \
    -v "/home/${USER}/${REPO_NAME}:/home/${USER_NAME}/${REPO_NAME}" \
    "${IMG}"