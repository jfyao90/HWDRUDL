from tensorflow.keras.models import load_model

import numpy as np
import cv2
from io import BytesIO
from PIL import Image
import base64
import re
import os
from PIL import ImageOps

def processImage(image):
    image = re.search(r'base64,(.*)', image).group(1)
    image = Image.open(BytesIO(base64.b64decode(image)))
    image = ImageOps.invert(image) #converting white background to black and black text to white like the mnist data
    image = np.array(image)
    image = cv2.resize(image,(28,28))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image = image.reshape(1,28,28,1)

    image = predicttheimage(image)

    return image

def predicttheimage(image):
    print(os.getcwd())
    model = load_model('model.h5')
    return model.predict_classes(image)[0]

def processNpredict(image):
    image = processImage(image)
    #image = predicttheimage(image)
    return image
