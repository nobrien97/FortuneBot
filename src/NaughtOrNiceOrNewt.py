	
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

def NaughtyOrNiceOrNewt(Str):
	model = tf.keras.models.load_model('./mhhh')
	img = Image.new('L',(200,200))
	pix = img.load()
	for i in range(200):
		if(i<len(Str)):
			pix[i,0] = (ceil(ord(Str[i])))
		else:
			pix[i,0] = 0
	fileName = "./tester.png"
	img.save(fileName)

	img = keras.preprocessing.image.load_img(
		"./tester.png", target_size=(200, 200)
	)
	img_array = keras.preprocessing.image.img_to_array(img)
	img_array = tf.expand_dims(img_array, 0) 

	predictions = model.predict(img_array)
	score = tf.nn.softmax(predictions[0])
	class_names = ['-1', '0', '1']
	return class_names[np.argmax(score)], 100 * np.max(score)


import discord
from os import system, path
from io import StringIO
from subprocess import getoutput
import sys
from random import randrange
from PIL import Image, ImageDraw, ImageFont
from math import ceil

client = discord.Client()

@client.event
async def on_ready():
	print('Fortune Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	
	if (message.content.find('!fortune ') != -1):
		msg = getoutput('fortune')
		userThreat = NaughtyOrNiceOrNewt(message.content)
		
		while userThreat == NaughtyOrNiceOrNewt(msg):
			print(msg)
			msg = getoutput('fortune')
		# Choose a random cow type from the list of all cowsay characters
		cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-animal characters
		cowTypes = cowTypes.split() # split into cowsay animals
		typechoice = cowTypes[randrange(0, len(cowTypes), 1)]
		# Use our choice to generate a cowsay
		msg = getoutput('cowsay {}'.format(msg))

		# Image generation: calculate length and width of image and instantiate
		msgFont = ImageFont.truetype("UbuntuMono-R.ttf", 12)
		msgDim = msgFont.getsize_multiline(msg)

		msgImg = Image.new('RGB', (ceil(msgDim[0] + 0.1*msgDim[0]), ceil(msgDim[1] + 0.1*msgDim[1])), (255, 255, 255))
		msgDraw = ImageDraw.Draw(msgImg)
		msgDraw.text((16, 0), msg, fill=(0, 0, 0, 255), font=msgFont)
		# TODO: Don't save to hard drive just to load again
		msgImg.save('/tmp/fortune.png')
		await message.channel.send(file=discord.File('/tmp/fortune.png'))
		await message.channel.send("{}".format(userThreat))

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('./DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)