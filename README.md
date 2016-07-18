Continuous integration with Drone using Docker
===============================================================================
Goal: Set up continuous integration testing of a Python app

CI server is set up on DigitalOcean (Ubuntu) using Docker

Reference Flask app: `picr`: upload a pic and return it, using a simple
Python/Flask app. See `/picr`

The CI tests to be ran are in `/picr/picr_tests.py`


Installation of the CI server on DO
===============================================================================
Create a repo with the files in `/picr`. See [its README](/picr/README.md) to deploy it to heroku.

Prepare Github access by following
[Step One on this link](https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker#step-one-—-prepare-github).




/root/droneio/drone.sqlite




References
===============================================================================
## Drone
https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker

## Flask
http://blog.shea.io/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku/
http://flask.pocoo.org/docs/0.10/testing/


