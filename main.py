from flask import Flask, request
from flask_cors import CORS
from preprocess import preProcess
from postprocess import postProcess, postProcessDebug

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  lang = request.form.get('lang')
  debug = request.form.get('debug')
  image_preprocessed = preProcess(file)
  if (debug):
    return postProcessDebug(image_preprocessed, lang)
  return postProcess(image_preprocessed, lang)

app.run(debug=True)


