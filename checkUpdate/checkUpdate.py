import urllib.request, urllib.parse, urllib.error
import json 
import os 
from subprocess import call

authUrl = "https://auth.docker.io/token?service=registry.docker.io&scope=repository:dbecker1/cs2110docker:pull"

authResponse = urllib.request.urlopen(authUrl)
authData = authResponse.read().decode()

try:
    authJs = json.loads(authData)
except:
    authJs = None

imageDataUrl = "https://registry-1.docker.io/v2/dbecker1/cs2110docker/tags/list";
dataRequest = urllib.request.Request(imageDataUrl)

dataRequest.add_header('Authorization', "Bearer " + authJs["token"]);

dataResponse = urllib.request.urlopen(dataRequest)
imageData = dataResponse.read().decode()

try:
    imageJs = json.loads(imageData)
except:
    imageJs = None

tags = imageJs["tags"]
mostRecentTag = "0.0.0"

for tag in tags:
	if tag == "latest":
		continue
	tag1Split = mostRecentTag.split(".")
	tag2Split = tag.split(".")
	i = 0
	if i < len(tag1Split) and i < len(tag2Split):
		if int(tag1Split[i]) < int(tag2Split[i]):
			mostRecentTag = tag
			break
	elif len(tag2Split) > len(tag1Split):
		mostRecentTag = tag
		break

currentVersion = os.environ['CS2110_IMAGE_VERSION']

if mostRecentTag != currentVersion:
	call(["notify-send", "'Update Docker Image'", "'Hello, your TAs have pushed an update to this Docker Image. In order to ensure you have the latest and greatest, please re-run the cs2110docker.sh script'"])
else:
	print("Docker image is up to date")