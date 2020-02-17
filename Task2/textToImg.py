# !/usr/bin/env python3
'''
Copyright @2020 Zhou Shen
HW 4 - #2
'''

import os
from PIL import Image, ImageDraw, ImageFont   # for text on image 

def textToImg(twitterText, twitterUsr, twitterNum):
  # convert / write text on image
  img = Image.new('RGB', (400, 150), color = (0, 0, 0))

  # font for windows user
  # font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
  d = ImageDraw.Draw(img)
  d.text((50,20), twitterText, fill=(255, 255, 255))

  fileName = "img/" + twitterUsr + str(twitterNum) + ".png"

  img.save(fileName)

## test use
#textToImg("hahaha", "BU", 1)
#textToImg("hhhhhh", "BU", 2)
