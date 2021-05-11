import os
import sys
import io
from subprocess import getoutput


os.system('clear')
cowTypes = getoutput('cowsay -l')[37:]

print(cowTypes)