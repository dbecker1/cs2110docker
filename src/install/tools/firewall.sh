#!/bin/bash
### every exit != 0 fails the script
set -e

echo "Install and configure firewall"
apt-get update
apt-get install -y ufw

ufw default deny outgoing
ufw default deny incoming

uwf default allow 6901
uwf default allow 5901