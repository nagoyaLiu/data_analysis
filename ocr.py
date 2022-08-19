from PIL import Image
import pyocr
import os
path = 'C:/Program files/Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path
tools = pyocr.get_available_tools()
tool = tools[0]

img = Image.open("nakata.png")
print(img)
