#!/usr/bin/env bash

REPOSITORY="argnctu/oop"
TAG="isaacgym"

IMG="${REPOSITORY}:${TAG}"

docker pull "${IMG}"
