Continuous integration with Drone using Docker
===============================================================================
[![Build Status](http://192.241.144.155:8080/api/badge/github.com/pavopax/ci-python-drone/status.svg?branch=master)](http://192.241.144.155:8080/github.com/pavopax/ci-python-drone)

Goal: Set up continuous integration testing of a Python app

CI server is set up on DigitalOcean (Ubuntu) using Docker

Reference Flask app: `picr`: upload a pic and return it, using a simple
Python/Flask app. See `/picr`

The CI tests to be ran are in `/picr/picr_tests.py`. This command appears in `.drone.yml`


Instructions
===============================================================================
It's easiest if you perform these steps on the DO box. Step 1 can be done locally, however.


(1)  
`sh deploy-heroku.sh`

Deploy the sample heroku app. See [its README](/picr/README.md) for details.

(2)

Push repo in (1) to github. It will be used in (8)

(3)

Prepare Github access for drone.io deployment by following
[Step One on this link](https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker#step-one-—-prepare-github).

(4)  
`cd droneio`

(5)  
Update oAuth keys in `Dockerfile` from (3)

(6)   
Verify that you are in this directory: `/root/droneio/`. Otherwise, edit
this path in `script.sh`

(7)  
`sh deploy-tests.sh`

Deploy drone.io task with docker. Check that it's running with
`docker ps`. Troubleshoot
[here](https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker#step-two-—-launch-the-drone-container)

(8)  

Visit [http://YOUR_DROPLET_IP:8080/login](http://YOUR_DROPLET_IP:8080/login)
and activate the repo from (2)

(9)
You can now run builds by pushing to the repo from (2). Docker will use the
image and run the commands specified in `.drone.yml`

Note: `node` image includes git. An alternative image is `nginx`.

Add scripts to test under `script` in `.drone.yml`



References 
===============================================================================
## Drone
https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker

## Flask
http://blog.shea.io/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku/
http://flask.pocoo.org/docs/0.10/testing/


