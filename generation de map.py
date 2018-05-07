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
Map = ["terre"]*taille_map      #défini la map comme etant de la terre a t0

entry = ["cactus","terre","terre","terre","terre"] # défini les possibilitées de spawn
def choix_terrain(Map): # fonction contenant les regles de generation de la map
    Map[taille_map-1]= rdm.choice(entry)
    if Map[taille_map-4:taille_map-1]== ["cactus"]*3:
        Map[taille_map-1 ]="terre"
    elif Map[taille_map-3:taille_map-1]== ["cactus","terre"]:
        Map[taille_map-1]="terre"
    elif Map [taille_map-4:taille_map-1]== ["cactus","terre","terre"]:
        Map[taille_map-1]="terre"
    elif Map[taille_map-5:taille_map-1]== ["cactus","terre","terre","terre"]:
        Map[taille_map-1]="terre"
        
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
    
    
print (Map) #affichage de la map a t 0
while not stop and en_vie:
    boucle = 1
    
    
    for i in range(taille_map-1):
        
        en_vie = GameOver(posDino,Map[9])    
        Map[i]= Map[i+1]
        if posDino == 0:
            Map[8] = "R"
        if Map[8] == "R":
            for i in range(8):
                Map[i]="terre"                
        else :
            Map[i]= Map[i+1] #décales toutes les entrées de la map vers la gauche
            
    print (en_vie)  
    choix_terrain(Map)
    if en_vie == 0:
        break 
    if posDino >= 1:
        posDino -= 1 # dino redescend
    print_MAP(Map) #affichage de la map
    choix = input()
    stop = ( choix == "stop")
    sauter =( choix == "sauter")
    posDino = saut(sauter, posDino)

print("Game Over")