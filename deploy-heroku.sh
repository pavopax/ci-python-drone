#!/bin/bash

echo "Deploying to heroku. Follow the commands..."

cd picr

git init

git add *

heroku login

heroku create

git push heroku master

heroku open

echo "DONE."
