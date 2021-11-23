import numpy as np
import cv2
from keras.models import load_model
from tensorflow.keras.applications import resnet50


def recognize_animal(path):
    model = load_model('model.h5')
    img = cv2.imread(path[1:])
    img = cv2.resize(img, (int(100), int(100)))
    img = resnet50.preprocess_input(img)
    img = img.reshape(1, 100, 100, 3).astype('float32')
    x = model.predict(img)
    return np.argmax(x, axis=1)[0]
