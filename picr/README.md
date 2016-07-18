Picr
===============================================================================
A Python/Flask app: upload a pic, and magically return it

Deployed to `heroku` at [http://picr-test.herokuapp.com](http://picr-test.herokuapp.com)

Manual steps to deploy this app are below. See  `../README.md` for an automatic script.


Installation
===============================================================================
Based on http://blog.shea.io/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku/

Prereqs: [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) 

1. Clone this repo
2. cd to directory containing `picr.py`
3. `virtualenv venv --distribute` to activate virtual environment
4. `source venv/bin/activate` 
5. `pip install Flask`
6. `pip freeze > requirements.txt`
7. `heroku login`, `heroku create` to create heroku app
8. `git commit` all changes
9. `git push heroku master`
10. `heroku open` to open the deployed heroku app

