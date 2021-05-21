# Test the model by feeding it some user input as an image	
from PIL import Image, ImageDraw, ImageFont
from math import ceil
import random
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


model = tf.keras.models.load_model('./mhhh')
Str = input("msg pls?")

# More information in newt_wordz_create.py
img = Image.new('L',(200,200))
pix = img.load()
for i in range(200):
	if(i<len(Str)):
		pix[i,0] = (ceil(ord(Str[i])))
	else:
		pix[i,0] = 0
fileName = "./tester.png"
img.save(fileName)

# Predict if the message was mean, nice, or neutral
img = keras.preprocessing.image.load_img(
    "./tester.png", target_size=(200, 200)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) 

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
class_names = ['-1', '0', '1']
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)