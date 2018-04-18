#!/usr/bin/env bash

if [ "$#" -ne 1 ];then
    echo "Usage:"
    printf "\t%s <image-name>\n" $0
    exit 1
fi

docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device /dev/video0 \
    $1
