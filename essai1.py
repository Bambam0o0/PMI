# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:00:51 2022

@author: delia
"""
import cv2, imageio, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


chemin = "C:\\Users\\delia\\Documents\\AERO 5\\PMI\\Machine Learning\\Reconnaissance printed digits\\images\\"

SCALE = 10
THICK = 5
WHITE = (255,255,255)

digits, numeros = [], []
for digit in map(str, range(10)):
    (width, height), bline = cv2.getTextSize(digit, cv2.FONT_HERSHEY_SIMPLEX,
                                             SCALE, THICK)
    digits.append(np.zeros((height + bline, width), np.uint8))
    cv2.putText(digits[-1], digit, (0, height), cv2.FONT_HERSHEY_SIMPLEX,
                SCALE, WHITE, THICK)
    x0, y0, w, h = cv2.boundingRect(digits[-1])
    digits[-1] = digits[-1][y0:y0+h, x0:x0+w]
    numeros.append(digits[-1])

#save image 
for i in range(len(numeros)):
    nom = chemin+'fleur'+str(i)+'.png'
    plt.imsave(str(nom), numeros[i])
#resize
    file = nom
    pil_file = Image.open(file)
    pil_file2 = pil_file.resize((60, 55), Image.ANTIALIAS)
    #pil_file2.show()
#change color
    pil_file2 = pil_file2.convert("La")
    #pil_file2.show()
#center numero

# def center_crop(pil_file2, dim):
#     width, height = pil_file2.shape[1], pil_file2.shape[0]
#     crop_width = dim[0] if dim[0]<pil_file2.shape[1] else pil_file2.shape[1]
#     crop_height = dim[1] if dim[1]<pil_file2.shape[0] else pil_file2.shape[0]
#     mid_x, mid_y = int(width/2), int(height/2)
#     cw2, ch2 = int(crop_width/2), int(crop_height/2) 
#     crop_img = pil_file2[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]

#     return crop_img



