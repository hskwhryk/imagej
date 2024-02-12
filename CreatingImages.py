from ij import ImagePlus  
from ij.process import FloatProcessor  
from array import zeros  
from random import random  
  
width = 1024  
height = 1024  
pixels = zeros('f', width * height)  
  
for i in xrange(len(pixels)):  
  pixels[i] = random()  
  
fp = FloatProcessor(width, height, pixels, None)  
imp = ImagePlus("White noise", fp)  
  
imp.show()  
