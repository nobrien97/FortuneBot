from math import ceil
from random import randrange
import numpy as np
import PIL
import tensorflow as tf
import pathlib

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import discord
from os import path
from subprocess import getoutput
from math import ceil


def NaughtyOrNiceOrNewt(Str):
# https://www.tensorflow.org/tutorials/images/classification
	model = tf.keras.models.load_model('./mhhh')
	img = PIL.Image.new('L',(200,200))
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


client = discord.Client()

@client.event
async def on_ready():
	print('Fortune Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	
	if (message.content.find('!fortune') != -1):
		# Choose a random cow type from the list of all cowsay characters
		cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-animal characters
		cowTypes = cowTypes.split() # split into cowsay animals
		typechoice = cowTypes[randrange(0, len(cowTypes), 1)]

		# Use our choice to generate a cowsay
		if message.content != '!fortune':
			msg = getoutput('fortune')
			userThreat = NaughtyOrNiceOrNewt(message.content)[0]
		
			while userThreat == NaughtyOrNiceOrNewt(msg)[0]:
				print(msg)
				msg = getoutput('fortune')
			msg = getoutput('echo {a} | cowsay -f {b}'.format(a=msg, b=typechoice))

		else:
			msg = getoutput('fortune | cowsay -f {}'.format(typechoice))

		# Image generation: calculate length and width of image and instantiate
		msgFont = PIL.ImageFont.truetype("UbuntuMono-R.ttf", 12)
		msgDim = msgFont.getsize_multiline(msg)

		msgImg = PIL.Image.new('RGB', (ceil(msgDim[0] + 0.1*msgDim[0]), ceil(msgDim[1] + 0.1*msgDim[1])), (255, 255, 255))
		msgDraw = PIL.ImageDraw.Draw(msgImg)
		msgDraw.text((16, 0), msg, fill=(0, 0, 0, 255), font=msgFont)
		# TODO: Don't save to hard drive just to load again
		msgImg.save('/tmp/fortune.png')
		await message.channel.send(file=discord.File('/tmp/fortune.png'))
		await message.channel.send("userThreat = {}".format(userThreat))

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('./DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)