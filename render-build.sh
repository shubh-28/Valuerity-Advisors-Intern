#!/bin/bash

# Update package lists
echo "Updating package lists..."
apt-get update

# Install build tools and dependencies
echo "Installing build tools and dependencies..."
apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    python3-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libffi-dev \
    libssl-dev

# Verify installation
echo "Verifying installation of critical libraries..."
dpkg -l | grep -E "libsdl2|build-essential|cmake|libopenblas-dev|liblapack-dev|python3-dev|libffi-dev|libssl-dev"

# Clean up unnecessary files
echo "Cleaning up..."
apt-get clean

echo "Script execution completed."
