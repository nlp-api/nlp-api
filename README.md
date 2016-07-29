# nlp-api
Natural Language Processing API

## Get flask running:
   - clone repo and `cd nlp-api/web/`.
   - start venv (download if you dont have it)
   - `export FLASK_APP=api.py`
   - `flask run`
   - You should now have the api running!
   `* Running on http://0.0.0.0:5000/`

## Run using `docker`
   - clone repo and `cd nlp-api/web/`.
   - if you don't have them, install docker
   - `docker build -t nlp-api:latest .`
   - `docker run -p 5000:5000 nlp-api`
   - You should now have the api running!
   `* Running on http://0.0.0.0:5000/`
   `http://localhost:5000/` also works.

## Run using `docker-compose`
   - clone repo and `cd nlp-api/`.
   - if you don't have them, install docker and docker-compose
   - `docker-compose build`
   - `docker-compose up`
   - You should now have the api running!
   `* Running on http://0.0.0.0:5000/`
   `http://localhost:5000/` also works.
