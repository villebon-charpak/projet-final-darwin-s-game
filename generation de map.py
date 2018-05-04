# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:29:32 2018

@author: etudiant
"""
import numpy as np
import random as rdm
t=0
taille_map=100
stop=False
boucle=1
liste = ["terre"]*taille_map
entry = ["cactus","terre","terre","terre","terre"]
def choix_terrain(liste):
    liste[taille_map-1]= rdm.choice(entry)
    if liste[taille_map-4:taille_map-1]== ["cactus"]*3:
        liste[taille_map-1 ]="terre"
    elif liste[taille_map-3:taille_map-1]== ["cactus","terre"]:
        liste[taille_map-1]="terre"
    elif liste [taille_map-4:taille_map-1]== ["cactus","terre","terre"]:
        liste[taille_map-1]="terre"
    elif liste[taille_map-5:taille_map-1]== ["cactus","terre","terre","terre"]:
        liste[taille_map-1]="terre"
def print_MAP(liste):
    s=""
    for terrain in liste:
        if terrain == "terre" :
            s+="_"
        else:
            s+="8"
    print(s)
print (liste)
while not stop:
    boucle = 1
    print("laaaa")
    
    for i in range(taille_map-1):
        liste[i]= liste[i+1]
        
    choix_terrain(liste)
    
    print_MAP(liste)
    stop = ( input() == "stop")
        
        

print("fini")