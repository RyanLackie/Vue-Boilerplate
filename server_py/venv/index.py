# Required modules
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests


# Settings
host = 'localhost'
#host = '134.209.217.37'
port = '82'
DEBUG = True
app = Flask(__name__)

# Enable CORS
CORS(app)


# Methods
@app.route('/ping', methods=['POST'])
def ping_pong():
    return jsonify('pong!')



# Run server
if __name__ == '__main__':
    app.run(host=host, port=port)