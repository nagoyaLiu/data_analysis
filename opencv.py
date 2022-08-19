import cv2
from matplotlib import pyplot as plt
import glob
import os


img = cv2.imread('nakata.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Img',img_gray)
img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#cv2.imshow('1',img_90)

#print(img.shape)

width =200
height= 200

#img_samll = cv2.resize(img, (width, height))

#cv2.imshow('1', img_samll)
file_path_list = glob.glob('syasinn/*')


print(file_path_list)


for file_path in file_path_list:
    img = cv2.imread(file_path)
    img_90 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow('1',img_90)
    

cv2.waitKey(0)