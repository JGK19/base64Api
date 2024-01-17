from flask import Flask, jsonify
import utils

app = Flask(__name__)

@app.route('/getB64/<string:x>', methods=['GET'])
def getB64(x):
  output = utils.binary_to_base64(x)
  return jsonify(output)

@app.route('/getB2from64/<string:x>', methods=['GET'])
def getB2from64(x):
  output = utils.base64_to_binary(x)
  return jsonify(output)

@app.route('/getB16/<string:x>', methods=['GET'])
def getB16(x):
  output = utils.base2_to_base16(x)
  return jsonify(output)

@app.route('/getB2from16/<string:x>', methods=['GET'])
def getB2from16(x):
  output = utils.base16_to_base2(x)
  return jsonify(output)
