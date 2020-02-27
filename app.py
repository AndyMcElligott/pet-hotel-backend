from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST', 'PUT'])
def hello_world():
  print(request)
  print('Hello World!')
  return 'Hello, World!'



