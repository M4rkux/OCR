from flask import Flask, request
from flask_cors import CORS
from preprocess import preProcess
from postprocess import postProcess, postProcessDebug

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  image_preprocessed = preProcess(file)
  response = postProcess(image_preprocessed)

  return response

@app.route("/debug", methods=['POST'])
def ocrDebug():

  file = request.files['image'].read()
  image_preprocessed = preProcess(file)
  response = postProcessDebug(image_preprocessed)

  return response


app.run(debug=True)


