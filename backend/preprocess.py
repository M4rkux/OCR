import numpy as np
import cv2
import skimage.filters as filters

def preProcess(file):
  img = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_UNCHANGED)

  inverted = cv2.bitwise_not(img)

  gray = cv2.cvtColor(inverted, cv2.COLOR_BGR2GRAY)

  # blur
  smooth = cv2.GaussianBlur(gray, (95,95), 0)

  # divide gray by morphology image
  division = cv2.divide(gray, smooth, scale=255)

  # sharpen using unsharp masking
  sharp = filters.unsharp_mask(division, radius=1.5, amount=1.5, multichannel=False, preserve_range=False)
  sharp = (255*sharp).clip(0,255).astype(np.uint8)


  # threshold
  _, thresh = cv2.threshold(sharp, 255, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  # Save image
  # cv2.imwrite('thresh.png',thresh)

  # show results
  # cv2.imshow('thresh', thresh)  
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  return thresh