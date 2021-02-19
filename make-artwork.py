# man, there are so many ways of making images in python... 
# I guess we start with openCV? 
import cv2 as openCV
import numpy as np

sidelength = 512 #typical AA size in iTunes
black = [0,0,0]
purple = [50,0,200] #RGB

def draw_gradient(image, colour1, colour2):
    [c1red, c1green, c1blue] = colour1
    [c2red, c2green, c2blue] = colour2
    
    for a in arange(image.size(axis=1)):

    return image



img = np.zeros([512,512])

print(img)
