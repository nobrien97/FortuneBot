'''
This script generates 'sentences' from random combinations of nice, mean, and neutral words, then 
converts those sentences into images by treating each character's unicode table index as a greyscale
value.
'''


from PIL import Image, ImageDraw, ImageFont
from math import ceil
import random
wholeAssFile_nice = open("./nice_wordz", 'r').read().split("\n")
wholeAssFile_mean = open("./mean_wordz", 'r').read().split("\n")
wholeAssFile_newt = open("./newt_wordz", 'r').read().split("\n")
for interator in range(3000):
	# Sentence length
	sent_len = random.randrange(1,10)
	# [nice, newt, mean]
	# How many words are we getting from each list?
	wordTotal = [random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)]
	# Sample the words
	wholeAssFile_list = random.sample(wholeAssFile_nice,wordTotal[0]) + random.sample(wholeAssFile_newt,wordTotal[1]) +random.sample(wholeAssFile_mean,wordTotal[2])
	# Weighting - a sentence's 'type' is the largest number of words of a given type in the sentence (e.g. [2, 4, 6] would be a mean sentence)
	weigth = wordTotal.index(max(wordTotal))-1
	shuff_l = random.sample(wholeAssFile_list,len(wholeAssFile_list))
	# Convert the array of words to a string
	Str = ' '.join([str(elem) for elem in shuff_l])

	# For TensorFlow to be happy, we need to feed a square image, so we pad a massive amount of it with 0s
	img = Image.new('L',(200,200))
	pix = img.load()
	for i in range(200):
		if(i<len(Str)):
			# ord(i) returns the unicode position of a character i as a float
			pix[i,0] = (ceil(ord(Str[i])))
		else:
			# Pad the end of the file with 0s
			pix[i,0] = 0

	fileName = "./data/"+str(weigth)+"/"+str(interator)+".png"
	img.save(fileName)