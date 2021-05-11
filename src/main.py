import discord
from os import system, path
from io import StringIO
from sys import stdout
from random import random

client = discord.Client()

@client.event
async def on_ready():
    print('Fortune Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if (message.content == '!fortune'):
        system('cowsay -l')
        stdout = cowtypes = StringIO()
        cowtypes = cowtypes[37:] # Remove the non-type characters
        cowtypes = cowtypes.split()
        typechoice = cowtypes[random(0, cowtypes.length())]
        system('clear')
        
        system('fortune | cowsay -f {}'.format(typechoice))
        stdout = msg = StringIO()
        await message.channel.send(msg)
        system('clear')

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('~/Projects/Discord/DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)