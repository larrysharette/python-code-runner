from flask import Flask, jsonify
from flask import request
from subprocess import Popen, PIPE, check_output
import shutil
import sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
  content = request.get_json()
  with open(content['filename'], 'w') as outfile:
    outfile.write(content['content'])
  p = Popen([sys.executable, content['filename']], stdout=PIPE, stderr=PIPE)
  output, err = p.communicate()
  return jsonify({"output": output, "err": err})