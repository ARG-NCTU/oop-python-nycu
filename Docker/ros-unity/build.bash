#!/usr/bin/env bash

REPOSITORY="argnctu/aoop_unity"
TAG="latest"

IMG="${REPOSITORY}:${TAG}"


# Get the full path and name of the script
# See https://bit.ly/3zHMisF
SCRIPT_NAME=$(basename "$BASH_SOURCE")

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  SCRIPT_PATH=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$SCRIPT_PATH/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPT_PATH=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

# Check if the Dockerfile exist

if [ -f "${SCRIPT_PATH}/dockerfile" ]; then
  DOCKERFILE_PATH="${SCRIPT_PATH}/dockerfile"
else
  echo "Parse Dockerfile path error"
  return 1
fi

echo "=================================================="
echo "Show Dockerfile:"
cat "$DOCKERFILE_PATH"
echo ""

echo "=================================================="
echo "Start building image"
docker build --rm -f "$DOCKERFILE_PATH" -t "${IMG}" $SCRIPT_PATH
