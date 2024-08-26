# MicroPy
Microservice in Python using Flask

# Steps
- Install Python3

- Create Virtual Environment
python3 -m venv .micropy.env
source ./.micropy.env/bin/activate

- Installing Python VSCode Extension

- Installing Flask
pip3 install Flask
# To show list of installed libraries
pip list

- Minimal Flask Application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

- Run Flask App
flask --app <<app-filename>> run
flask --app myapp run --host=0.0.0.0

# Using Environment Variable
set FLASK_APP=myapp
flask run --host=0.0.0.0

# Rendering Template
Create templates

# Freeze Dependencies
pip3 freeze > requirements.txt
# To install dependencies
pip3 install -r requirements.txt

# Running Docker Standalone
docker build -t micropy:1.0 .
docker run -d -p 7789:5000 --name micropy micropy:1.0

# Tag on DockerHub
docker tag pmittal77/micropy 

# Running docker inside Minikube
Install minikube and kubectl

# Minikube Run and Delete
# To Start
minikube start
minikube ip
# Expose to external IP
minikube tunnel

# Deploy app and app service

# To get docker environment variables
minikube docker-env
# To Delete
minikube delete
