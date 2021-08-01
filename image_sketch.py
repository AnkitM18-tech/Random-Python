import numpy as np
import imageio as io
import cv2
import scipy.ndimage

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

img="ankit_test.jpg"
read_img=io.imread(img)
g=grayscale(read_img)
sketch_img=255-g
b=scipy.ndimage.filters.gaussian_filter(sketch_img,sigma=10)
r=dodge(b,g)

cv2.imwrite("sketch.png",r)