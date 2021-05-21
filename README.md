# empathBot

empathBot is the dumbest use for image-based neural networks ever devised. It reads text converted to images to decide whether
that text was hurtful, pleasant, or neutral. The network is trained on randomly generated combinations of nasty (-1), neutral (0),
and nice (1) words, with each sentence's niceity being based on the number of -1, 0, and 1 words in it.
For example a nice sentence contains more 'nice' words than both neutral and nasty words.

Text is converted to images by taking each sentence's characters and converting them to unicode table indices. These indices are used
as greyscale colour values that are added pixel by pixel into an image. Since TensorFlow requires some more data than a 1px high image,
we pad the image to 200x200 with black.

The grand result is a neural network that can read sentences that Discord users send it and respond with an appropriate fortune from the 
```fortune-mod``` package. Does it work? Far better than it should given the quality of the training data and the hacky code. 
But still not very well.

## Dependencies:
- discord.py ```python -m pip install -U discord.py```
- Pillow ```python -m pip install --upgrade Pillow```
- TensorFlow and probably TensorFlow-gpu ```python -m pip install -U tensorflow tensorflow-gpu```
- numpy ```python -m pip install -U numpy```
- fortune and cowsay ```sudo apt install fortune-mod cowsay```
- An NVidia GPU
