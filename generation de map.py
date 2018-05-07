# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:29:32 2018

@author: etudiant
"""
import numpy as np
import random as rdm

posDino = 0
en_vie = 1
taille_map=40    #defini la longueur de la map
stop=False       # bouléen pour stoper le programme
boucle=1    #variable du while permettant de le break
liste = ["terre"]*taille_map      #défini la map comme etant de la terre a t0

entry = ["cactus","terre","terre","terre","terre"] # défini les possibilitées de spawn
def choix_terrain(liste): # fonction contenant les regles de generation de la map
    liste[taille_map-1]= rdm.choice(entry)
    if liste[taille_map-4:taille_map-1]== ["cactus"]*3:
        liste[taille_map-1 ]="terre"
    elif liste[taille_map-3:taille_map-1]== ["cactus","terre"]:
        liste[taille_map-1]="terre"
    elif liste [taille_map-4:taille_map-1]== ["cactus","terre","terre"]:
        liste[taille_map-1]="terre"
    elif liste[taille_map-5:taille_map-1]== ["cactus","terre","terre","terre"]:
        liste[taille_map-1]="terre"
        
def print_MAP(liste): # covertisseur de texte en interface graphique
    s=""
    for terrain in liste:
        if terrain == "R":
            s+= "R"
        
        elif terrain == "terre" :
            s+="_"
        elif terrain == "cactus" :
            s+="8"
    print(s)
def saut(sauter, posDino):
    if sauter ==0:
        return posDino
    else :
        if posDino == 0:
            return 5
        else :
            return posDino
    
def GameOver(posDino,terrain): 
    if terrain == "cactus" and posDino == 0:
        return 0
    else :
        return 1
    
    
print (liste) #affichage de la map a t 0
while not stop and en_vie:
    boucle = 1
    
    
    for i in range(taille_map-1):
        
        en_vie = GameOver(posDino,liste[9])    
    
        if posDino == 0:
            liste[8] = "R"
        else :
            liste[8] = liste[9]
        if liste[8] == "R":
            liste[i]= liste[i+1]
            for i in range(8):
                liste[i]="_"                
        else :
            liste[i]= liste[i+1] #décales toutes les entrées de la lite vers la gauche
            
    print (en_vie)  
    choix_terrain(liste)
    if en_vie == 0:
        break 
    if posDino >= 1:
        posDino -= 1 # dino redescend
    print_MAP(liste) #affichage de la map
    choix = input()
    stop = ( choix == "stop")
    sauter =( choix == "sauter")
    posDino = saut(sauter, posDino)

print("Game Over")