#!/bin/bash

echo "Deploying drone..."

touch drone.sqlite

docker run -d --name="drone-ci" -p 8080:8080 -v /var/lib/drone/ -v /var/run/docker.sock:/var/run/docker.sock -v /root/droneio/drone.sqlite:/var/lib/drone/drone.sqlite my_drone

echo "DONE. Test with <docker ps>"
