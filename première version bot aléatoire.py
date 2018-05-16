# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:14:18 2018

@author: etudiant
"""

import random as rdm
import numpy as np

def nonlin(x,deriv=False):

    if(deriv==True):

        return x*(1-x)

    return 1/(1+np.exp(-x))

def nb_cactus(MAP,distance):
    i=2+distance
    largeur=0
    while i < taille_map and Map[i]=='cactus':
        largeur+=1
        i+=1
    return largeur
       
    

def distance_next_cactus(liste_map):
    i=2
    distance=0
    while  (i < taille_map-1 ) and (Map[i]=='terre' or Map[i]=='R'):
        i+=1
        distance+=1
    return distance

def choix_robot(Map):
    if posDino == 0:
        if poids_distance*distance_bis + poids_largeur_cactus*largeur_cactus < 1:
            return 'sauter'
        else:
            return 'continue'
    else: return ('on continue de sauter')
    


#distance = nonlin(rdm.choice([1,2,3,4,5,6,7,8]))
#largeur_cactus =nonlin(rdm.choice([1,2,3]))

poids_distance=(rdm.randint(0,1000))/1000
poids_largeur_cactus=(rdm.randint(0,1000))/1000



        




case_depart = 2
score = 2
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
        
def print_MAP(Map, posDino): # covertisseur de texte en interface graphique
    s=""
    for terrain in Map:
        if terrain == "R":
            s+= "R"
        
        elif terrain == "terre" :
            s+="_"
        elif terrain == "cactus" :
            s+="8"
    if posDino == 0 :
        print("")
    else:
        print(" "*case_depart + "°")
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
    if posDino >= 1:
        posDino -= 1 #dino redescend
    en_vie = GameOver(posDino,Map[case_depart+1])
    for i in range(taille_map-1):
        Map[i]= Map[i+1]
        
        if posDino == 0:
            Map[case_depart] = "R"
        if Map[case_depart] == "R":
            for i in range(case_depart):
                Map[i]="terre"                
        else :
            
            Map[i]= Map[i+1] #décales toutes les entrées de la map vers la gauche
    score += 1  
    print (en_vie)  
    choix_terrain(Map)
    if en_vie == 0:
        break 
  
    #affichage de la map
    print_MAP(Map, posDino)
    distance = distance_next_cactus(Map)
    distance_bis= nonlin(distance)
    largeur_cactus = nb_cactus(Map,distance)
    choix = choix_robot(Map)
   #choix = input()
    print ('distance au cactus:', distance)
    print ('distance au cactus traitée:',distance_bis)
    print ('taille next obstacle is:', largeur_cactus)
    print (poids_distance*distance_bis + poids_largeur_cactus*largeur_cactus)
    stop = ( choix == "stop")
    sauter =( choix == "sauter")
    posDino = saut(sauter, posDino)

print("Game Over")
print("vous avez scoré",score,"!")

