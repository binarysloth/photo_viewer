import sys

from PIL import Image


filename = sys.argv[1]
img = Image.open(filename)
img.show()