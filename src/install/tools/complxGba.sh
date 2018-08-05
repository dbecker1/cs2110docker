#!/usr/bin/env bash
### every exit != 0 fails the script
set -e

echo "Install complx"
apt-get update
apt-get install -y software-properties-common
add-apt-repository ppa:tricksterguy87/ppa-gt-cs2110
apt update
apt install -y complx-tools
apt install -y gcc-arm-none-eabi cs2110-vbam-sdl cs2110-gba-linker-script nin10kit