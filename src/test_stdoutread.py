# Test file for calculating width and length, and drawing/saving image

import os
import sys
import io
from subprocess import getoutput
from PIL import Image, ImageDraw, ImageFont
from random import randrange
from math import ceil



os.system('clear')
cowTypes = getoutput('cowsay -l')[37:]

os.system('clear')
cowTypes = getoutput('cowsay -l')[37:] #  Remove the non-type characters
cowTypes = cowTypes.split()
typechoice = cowTypes[randrange(0, len(cowTypes), 1)]
os.system('clear')
msg = getoutput('fortune | cowsay -f {}'.format(typechoice))

msgFont = ImageFont.truetype("DejaVuSansCondensed-BoldOblique.ttf", 12)
msgDim = msgFont.getsize_multiline(msg)
print(msgDim)

msg_length = (msg.count('\n') * 16 ) + ceil(msg.count('\n') * 1/16 )
msg_width = ceil(msgFont.getsize(max(msg.split('\n')))[0]*1.5)
print(msg_width)
print(msg_length)
print(msg.split('\n'))


msgImg = Image.new('RGB', (ceil(msgDim[0] + msgDim[0]*0.1), ceil(msgDim[1] + msgDim[1]*0.1)), (255, 255, 255))
msgDraw = ImageDraw.Draw(msgImg)

msgDraw.text((16, 0), msg, fill=(0, 0, 0, 255), font=msgFont)

msgImg.save('test.jpg')
