#!/bin/sh

docker run -it --rm \
    -e GOOGLE_APPLICATION_CREDENTIALS=/usr/src/etc/service_account.json \
    -v $(pwd):/usr/src \
    -w /usr/src \
    python:3.7 \
    /bin/bash
