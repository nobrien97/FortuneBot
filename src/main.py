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

    
    if (message.content == '!fortune'):
        # Choose a random cow type from the list of all cowsay characters
        cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-animal characters
        cowTypes = cowTypes.split() # split into cowsay animals
        typechoice = cowTypes[randrange(0, len(cowTypes), 1)]
        # Use our choice to generate a cowsay
        msg = getoutput('fortune | cowsay -f {}'.format(typechoice))

        # Image generation: calculate approximate length and width of image (12 font size = 16px)
        msg_length = (msg.count('\n') * 16 ) + ceil(msg.count('\n') * 1/16 )
        msg_width = len(max(msg.split('\n')) * 8)  + ceil(len(max(msg.split('\n'))) * 2)
        msgImg = Image.new('RGB', (msg_width, msg_length), (255, 255, 255))
        msgDraw = ImageDraw.Draw(msgImg)
        msgFont = ImageFont.truetype("UbuntuMono-R.ttf", 12)
        msgDraw.text((16, 0), msg, fill=(0, 0, 0, 255), font=msgFont)
        # TODO: Don't save to hard drive just to load again
        msgImg.save('/tmp/fortune.png')
        await message.channel.send(file=discord.File('/tmp/fortune.png'))

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('~/Projects/Discord/DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)