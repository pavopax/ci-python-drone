#!/bin/bash

echo "Deploying to heroku. Follow the commands..."

cd picr

git init

git add *

git commit -am '[initial] initial commit'

heroku login

heroku create

git push heroku master

heroku open

echo "DONE."
