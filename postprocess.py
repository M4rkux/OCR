import pytesseract
from pytesseract.pytesseract import Output
import json

MIN_CONF = 10.0
CONFIG_TESSERACT = '--tessdata-dir tessdata/'
LANG='eng+por'

GAP_TOP = 40
GAP_LEFT = 200
GAP_INIT_LEFT = 35

def getValues(data, layout):
  result = ''
  for i in range(0, len(data['text'])):
    confidence = float(data['conf'][i])
    if (confidence > MIN_CONF and len(data['text'][i]) > 0):
      if (
          (layout['top'] < data['top'][i] and layout['top'] + GAP_TOP >= data['top'][i]) and
          ((layout['left'] - GAP_INIT_LEFT <= data['left'][i] and layout['left'] + GAP_LEFT >= data['left'][i]))):
        result += data['text'][i] + ' '

  return result.strip()

def prepareLayout(data, title):
  result = dict()
  for i in range(0, len(data['text'])):
    confidence = float(data['conf'][i])
    if (confidence > MIN_CONF and len(data['text'][i]) > 0):
      if (title.upper() == data['text'][i].upper()):
        content = dict()
        content['top'] = data['top'][i]
        content['left'] = data['left'][i]
        content['text'] = data['text'][i]
        if (title in result):
          currentContent = result[title]
          currentTop = currentContent['top']
          if (currentTop > data['top'][i]):
            result[title] = content
        else:
          result[title] = content

  return result

def postProcess(image): 
  pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
  data = pytesseract.image_to_data(image, lang=LANG, config=CONFIG_TESSERACT, output_type=Output.DICT)

  f = open('layouts/titles.json')
  titles = json.loads(f.read())
  f.close()

  response = ''
  layouts = dict()

  for title in titles:
    layout = prepareLayout(data, title)
    if (layout):
      layouts.update(layout)

  for title in layouts:
    content = getValues(data, layouts[title])
    if (len(content) > 0):
      response += layouts[title]['text'] + ': ' + content + '; '

  return {"response": response.strip()}

######################################################## POST PROCESS Debug ########################################################

def postProcessDebug(image):
  pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
  data = pytesseract.image_to_data(image, lang=LANG, config=CONFIG_TESSERACT, output_type=Output.DICT)

  result = []
  for i in range(0, len(data['text'])):
    confidence = float(data['conf'][i])
    if (confidence > MIN_CONF and len(data['text'][i]) > 0):
      obj = dict()
      obj['top'] = data['top'][i]
      obj['left'] = data['left'][i]
      obj['text'] = data['text'][i]
      obj['conf'] = data['conf'][i]
      result.append(obj)


  return json.dumps(result)