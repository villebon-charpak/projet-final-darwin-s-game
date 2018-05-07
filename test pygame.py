# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:09:56 2018
C:\Users\etudiant\Documents\Anaconda3\Scripts>set PATH=%PATH%;C:\Python27\ commande utile
@author: etudiant
"""

import pygame
from pygame.locals import *
pygame.init()
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6                     #Un nouvel écran vierge
 # Copie de l'arrière-plan sur l'écran
for i in range(6):
    screen[i] = background[i]
print (screen)
[1, 1, 2, 2, 2, 1]
 # Positionnement du héros sur l'écran
playerpos = 3
screen[playerpos] = 8
# Affichage du résultat
print (screen)
[1, 1, 2, 8, 2, 1]
