# https://www.tensorflow.org/tutorials/images/classification 
'''
This is a really dumb CNN model that works on images that are actually text.
Each character in the text has its unicode table index converted to a grayscale 
range and that is mapped as a single pixel. The data itself is encoded into a 
1px high and Xpx wide png, where X is the number of characters in the text being 
converted. The image is padded with 0s (black) to reach a 200x200 image size.
This process is done in newt_wordz_create.py

The text itself is random combinations of so called 'mean' 'nice' or 'neutral' words,
with 'mean' sentences containing more mean words than nice or neutral. The model is
"able" to predict which sentences are insulting or pleasant based on these datasets,
which can be used to give a response 
'''
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from tensorflow.keras import layers
import pathlib

# Import our ''''''''high quality'''''' training data
data_dir = pathlib.Path("./data")

# Images are 200x200, but the data is actually far less, but it's fine
batch_size = 128
img_height = 200
img_width = 200

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=1488882809,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=1564142324,
  image_size=(img_height, img_width),
  batch_size=batch_size,)



class_names = train_ds.class_names
print(class_names)

# Normalise image channel colour from 0-255 to 0-1
normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))

# Run-time tuning of number of images to prefetch
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


# 3 classes: 'mean', 'neutral', 'nice'
#              -1        0         1

num_classes = 3

# How may convolution layers? I don't know, just add a few I guess
# Model in da GPU, what features will he keep?
model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255),
  layers.Conv2D(32, 3, activation='relu',padding="same"),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu',padding="same"),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, activation='relu',padding="same"),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(32, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=50
)

model.save('./mhhh')
