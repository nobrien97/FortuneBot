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

    
    if (message.content.find('!fortune') != -1):
        # Choose a random cow type from the list of all cowsay characters
        cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-animal characters
        cowTypes = cowTypes.split() # split into cowsay animals
        typechoice = cowTypes[randrange(0, len(cowTypes), 1)]
        # Use our choice to generate a cowsay
        msg = getoutput('fortune | cowsay -f {}'.format(typechoice))

        # Image generation: calculate length and width of image and instantiate
        msgFont = ImageFont.truetype("UbuntuMono-R.ttf", 12)
        msgDim = msgFont.getsize_multiline(msg)

        msgImg = Image.new('RGB', (ceil(msgDim[0] + 0.1*msgDim[0]), ceil(msgDim[1] + 0.1*msgDim[1])), (255, 255, 255))
        msgDraw = ImageDraw.Draw(msgImg)
        msgDraw.text((16, 0), msg, fill=(0, 0, 0, 255), font=msgFont)
        # TODO: Don't save to hard drive just to load again
        msgImg.save('/tmp/fortune.png')
        await message.channel.send(file=discord.File('/tmp/fortune.png'))

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('~/Projects/Discord/DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)