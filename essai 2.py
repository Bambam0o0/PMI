
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:48:51 2022

@author: delia
"""

import imageio
import numpy
from matplotlib.pyplot import *

chemin = chemin = "C:\\Users\\delia\\Documents\\AERO 5\\PMI\\Machine Learning\\Reconnaissance printed digits\\"
nom = chemin+'parking_lot_no_car_2.png'
img = imread(nom)

print(img.shape)
print(img.dtype)

rouge = img[:,:,0]
vert = img[:,:,1]
bleu = img[:,:,2]

#print(vert)
#imshow(vert)
#colorbar()
print("")
print("")
print("")
print("nombre de pixels verts")
print("")
print("")
print("")

#on calcule le nombre de pixels verts sur l'image
def couleur(image):
    p = numpy.zeros(256,dtype=numpy.float32)
    t = image.shape
    for j in range(t[0]):
        for i in range(t[1]):
            valeur = image[j,i]
            p[int(valeur*255)] += 1
    return p
    
p = couleur(vert)
print(p)

#calculer le nombre de zéros sous forme de matrice 
zeros = p[numpy.where(p == 0)]
print(zeros)
print("Number of Zeroes in Matrix -->",zeros)

print('bonjour')

#on affiche le nombre de zéro
taille = zeros.size 
print(taille)
valmin = 50
valmax = 62 
#on détermine des valeurs seuils 
statut = 0
if (taille>=valmin and taille<=valmax) :  
    print ("place libre")
    statut = 0
else : 
    print('place occupée')
    statut = 1

    #la boucle if doit être une fonction, et à la fin faire une if name = main. Faire que des fonctions, mettre des return True/False. Eliminer tous les 'print'
    #épurer le code. OKAY :)

# chemin = "C:\\Users\\delia\\Documents\\AERO 5\\PMI\\Machine Learning\\Reconnaissance printed digits\\images\\"
# for i in range(0, 10, 1):
#     img = Image.new('RGB', (150,150), color = (0,0,0))
#     #font = ImageFont.load("arial.pil")
#     d = ImageDraw.Draw(img)
#     font = ImageFont.truetype("arial.ttf",100)
#     d.text((45,25), str(i), font = font, fill=(255,255,255))
#     #font = ImageFont.truetype("arial.ttf",20)
#     img.save (chemin+'joncquille'+str(i)+'.png')


    # myimg = cv2.imread('joncquille0.jpg') # image de la webcam
    # avg_color_per_row = numpy.average(myimg, axis=0)
    # avg_color = numpy.average(avg_color_per_row, axis=0)
    # print(avg_color)

# base = "joncquille01"
# sauvegarde = chemin + "modification.jpg + "


# def couleur_image(nom): 
#     ref_image = Img.open(nom)
#     largeur, hauteur = ref_image.size
#     for x in range (largeur): 
#         for y in range (hauteur): 
#            red, green, blue = ref_image.getpixel((x,y))
#     return ref_image 
#     print (ref_image)

# #place occupée voiture rouge
# nom = nom = chemin+'vertoccuperouge.jpg'
# img = Image.open(nom)
# largeur_image = 410
# hauteur_image = 234
# valmin = 245
# valmax = 260
# for y in range(hauteur_image):
#     for x in range(largeur_image): 
#         r,v,b=img.getpixel((x,y))
#         print("rouge : ", r, "vert :",v, "bleu",b)

# if (v>=valmin and v<=valmax and r!= 50 and b != 50):
#     print ("place libre")

# else : 
#     print ("place occupée")

# print("fin")

