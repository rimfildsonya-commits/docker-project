#!/bin/bash
if [ "$1" = "create_local_data" ]; then
    mkdir -p local_data
    python3 generator/generate.py ./local_data
elif [ "$1" = "build_generator" ]; then
    docker build -t generator-image ./generator
elif [ "$1" = "run_generator" ]; then
    mkdir -p data
    docker run -v $(pwd)/data:/data generator-image
elif [ "$1" = "build_reporter" ]; then
    docker build -t reporter-image ./reporter
elif [ "$1" = "run_reporter" ]; then
    docker run -v $(pwd)/data:/data reporter-image
elif [ "$1" = "structure" ]; then
    ls -la
elif [ "$1" = "clear_data" ]; then
    rm data/*
elif [ "$1" = "inside_generator" ]; then
    docker run -v $(pwd)/data:/data generator-image ls /data
elif [ "$1" = "inside_reporter" ]; then
    docker run -v $(pwd)/data:/data reporter-image ls /data
else
    echo " "
fi