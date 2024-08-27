#!/usr/bin/env bash

REPOSITORY="argnctu/oop"
TAG="isaacsim"

IMG="${REPOSITORY}:${TAG}"

# Get the full path and name of the script
# See https://bit.ly/3zHMisF
SCRIPT_NAME=$(basename $BASH_SOURCE)

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  SCRIPT_PATH=$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$SCRIPT_PATH/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPT_PATH=$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)

# Check if the Dockerfile exist

if [ -f "${SCRIPT_PATH}/Dockerfile" ]; then
  DOCKERFILE_PATH="${SCRIPT_PATH}/Dockerfile"
elif [ -f "${SCRIPT_PATH}/dockerfile" ]; then
  DOCKERFILE_PATH="${SCRIPT_PATH}/dockerfile"
else
  echo "Parse dockerfile path error: dockerfile not found"
  return -1
fi

echo "=================================================="
BOAD_GREEN="\033[1;32m"
END_COLOR="\033[0m"
echo -e "Show Dockerfile:${BOAD_GREEN}"
echo -e ""
cat "${DOCKERFILE_PATH}"
echo -e "${END_COLOR}"

echo "=================================================="
echo "Start building image"

docker buildx build --rm "$@" -f "${DOCKERFILE_PATH}" --load -t "${IMG}" "${SCRIPT_PATH}" 
