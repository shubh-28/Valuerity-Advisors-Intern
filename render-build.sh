#!/bin/bash

# Update package lists
apt-get update

# Install build tools and dependencies
apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    python3-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev
