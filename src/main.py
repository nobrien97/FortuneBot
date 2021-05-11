import discord
from os import system, path
from io import StringIO
from subprocess import getoutput
import sys
from random import randrange

client = discord.Client()

@client.event
async def on_ready():
    print('Fortune Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if (message.content == '!fortune'):
        system('clear')
        cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-type characters
        cowTypes = cowTypes.split()
        typechoice = cowTypes[randrange(0, len(cowTypes), 1)]

        system('clear')
        msg = getoutput('fortune | cowsay -f {}'.format(typechoice))
        await message.channel.send(msg)
        system('clear')

# Yeah nah not letting you lot see my ~ultra secret~ Discord Token(tm)
tokFile = open(path.expanduser('~/Projects/Discord/DISCORD_TOKEN.tok'))
DISCORD_TOKEN = tokFile.read()
tokFile.close()
client.run(DISCORD_TOKEN)