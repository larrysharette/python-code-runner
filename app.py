from flask import Flask, jsonify, request
from subprocess import Popen, PIPE
import sys
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
  content = request.get_json()
  with open(content['filename'], 'w') as outfile:
    outfile.write(content['content'])
  p = Popen([sys.executable, content['filename']], stdout=PIPE, stderr=PIPE, universal_newlines=True)
  output, err = p.communicate()
  os.remove(content['filename'])
  return jsonify({"output": output, "err": err})