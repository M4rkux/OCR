import os
from flask import Flask, request
from flask_cors import CORS
from preprocess import preProcess
from postprocess import postProcess, postProcessDebug

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def ocr():

  file = request.files['image'].read()
  debug = request.form.get('debug')
  image_preprocessed = preProcess(file)
  if (debug):
    return postProcessDebug(image_preprocessed)
  return postProcess(image_preprocessed)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


