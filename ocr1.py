from PIL import Image
import pyocr
import os
path = 'C:/program files/Tesseract-OCR'
os.environ['path'] = os.environ['path'] + path
tools = pyocr.get_available_tools()

tool = tools[0]

img = Image.open("nakata.png")

builder = pyocr.builder.TextBuilder(tesseract_layout =6)
text =tool.image_to_string(img,lang='jpn',builder = builder)

text = text.replace('','')
print(text)