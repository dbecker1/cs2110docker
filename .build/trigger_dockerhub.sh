#!/usr/bin/env bash
set -e -o pipefail

echo "trigger dockerhub builds for Tag $DOCKER_TAG:"

URLS=(
)
PAYLOAD='{"source_type": "Tag", "source_name": "'$DOCKER_TAG'"}'

if [[ $DOCKER_TAG == "latest" ]] ; then
    echo "DockerHub will not be triggered: use script 'tag_image.sh'"
    #PAYLOAD='{"docker_tag": "'latest'"}'
    exit 0
fi
if [[ $DOCKER_TAG == "dev" ]] ; then
   PAYLOAD='{"docker_tag": "'dev'"}'
fi

#Loop
for URL in "${URLS[@]}"
do
	echo "URL: $URL"
  	echo "PAYLOAD: $PAYLOAD"
    curl -H "Content-Type: application/json" --data "$PAYLOAD" -X POST "$URL"
    echo " - done!"
done