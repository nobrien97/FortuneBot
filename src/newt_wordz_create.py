
from PIL import Image, ImageDraw, ImageFont
from math import ceil
import random
wholeAssFile_nice = open("./nice_wordz", 'r').read().split("\n")
wholeAssFile_mean = open("./mean_wordz", 'r').read().split("\n")
wholeAssFile_newt = open("./newt_wordz", 'r').read().split("\n")
for interator in range(3000):
	sent_len = random.randrange(1,10)
	# [nice, newt, mean]
	wordTotal = [random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)]
	wholeAssFile_list = random.sample(wholeAssFile_nice,wordTotal[0]) + random.sample(wholeAssFile_newt,wordTotal[1]) +random.sample(wholeAssFile_mean,wordTotal[2])
	weigth = wordTotal.index(max(wordTotal))-1
	shuff_l = random.sample(wholeAssFile_list,len(wholeAssFile_list))

	Str = ' '.join([str(elem) for elem in shuff_l])

	img = Image.new('L',(200,200))
	pix = img.load()
	for i in range(200):
		if(i<len(Str)):
			pix[i,0] = (ceil(ord(Str[i])))
		else:
			pix[i,0] = 0
	fileName = "./data/"+str(weigth)+"/"+str(interator)+".png"
	img.save(fileName)