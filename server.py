import os
from flask import Flask
server = Flask(__name__)

@server.route("/")
def welcome():
    return "Welcome to devopswithcloud training"

@server.route('/openshift')
def hello():
    return 'Openshift is easy to learn'

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)