# FortuneBot

Thought I should learn some Python, so here's a Discord bot that runs the classic Linux ```fortune | cowsay```, randomly choosing an animal and posting the result as an image. The reason it's an image rather than text is to avoid funky character limits and ensure it draws properly. 
To use Fortune Bot, run ```main.py``` with a local token for a Discord bot with reading and posting permissions and then have anyone post ```!fortune```.

## Dependencies:
- Python 3.8.10
- discord.py ```python3.8 -m pip install -U discord.py```
- Pillow ```python3.8 -m pip install --upgrade Pillow```
- fortune and cowsay ```sudo apt install fortune-mod cowsay```
