# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:02:26 2018

@author: etudiant
"""

import numpy as np
import pygame
import random as rdm
import time
from pygame.locals import *
pygame.init()




def nonlin(x,deriv=False):#renvoie une valeur entre 0 et 1 en faisant passer l'entrée par une sigmoide 

    if(deriv==True):

        return x*(1-x)

    return 1/(1+np.exp(-x))

def nb_cactus(MAP,distance):#calcul le nombre de cactus du prochain obstacle 
    i=2+distance
    largeur=0
    while i < taille_map and Map[i]=='cactus':
        largeur+=1
        i+=1
    return largeur

def distance_next_pigeon(liste_map):#calcul la distance au prochain pigeon
    i=3
    distance2=0
    while  i < taille_map-1  and liste_map[i]=='air':
        i+=1
        distance2+=1
    return distance2
       
    

def distance_next_cactus(liste_map):#calcul la distance au prochain cactus
    i=2
    distance=0
    while  (i < taille_map-1 ) and (liste_map[i]=='terre' or liste_map[i]=='R'):
        i+=1
        distance+=1
    return distance

def choix_robot(Map):# le robot saute ou non en fonction du resultat de la sortie du reseau neuronal
    if posDino == 0:
        if poids_distance*distance_bis + poids_largeur_cactus*largeur_cactus + poids_distance2*distance2_bis > 1.5:
            return K_SPACE
        else:
            return 'nothing'
    else: return ('on continue de sauter')
    
def indice_seaker():#donne l'indice de la plus haute valeur de la liste_test
    for i in range(taille_test):
        if liste_test[i]==max(liste_test):
            return i
 
def meilleur(i):
    return liste_test[i]
    
def premiers_poids():#defini les premiers poids aléatoirement
    L=[0]*taille_test
    for i in range(taille_test):
        L[i]=[rdm.randint(0,1000)/1000,rdm.randint(0,1000)/1000,rdm.randint(0,1000)/1000]
    return L
    
def crea_liste_de_liste():#cree une liste de liste (sans le probleme: T=[L,L,L,L,L....] avec L=[a,b,c] (L constante))
    L=[0]*taille_test
    for i in range(taille_test):
        L[i]=[0,0,0]
    return L

def croisement_genome():#defini les prochains poids a partir des poids de la gene precedente
    for poids in range(taille_test-(taille_test/2)):
        poids[0]=((liste_poids[i_1][0]+liste_poids[i_2][0])/2)+(rdm.randint(-100,100)/1000)
        poids[1]=((liste_poids[i_1][1]+liste_poids[i_2][1])/2)+(rdm.randint(-100,100)/1000)
        poids[2]=((liste_poids[i_1][2]+liste_poids[i_2][2])/2)+(rdm.randint(-100,100)/1000)
    for poids in range(taille_test/2):
        

def choix_terrain(Map):  # fonction contenant les regles de generation de la map
    Map[taille_map - 1] = rdm.choice(entry)
    if Map[taille_map - 4:taille_map - 1] == ["cactus"] * 3:
        Map[taille_map - 1] = "terre"
    elif Map[taille_map - 3:taille_map - 1] == ["cactus", "terre"]:
        Map[taille_map - 1] = "terre"
    elif Map[taille_map - 4:taille_map - 1] == ["cactus", "terre", "terre"]:
        Map[taille_map - 1] = "terre"
    elif Map[taille_map - 5:taille_map - 1] == ["cactus", "terre", "terre", "terre"]:
        Map[taille_map - 1] = "terre"
    elif Map[taille_map - 6:taille_map - 1] == ["cactus", "terre", "terre", "terre", "terre"]:
        Map[taille_map - 1] = "terre"
    elif Map[taille_map - 7:taille_map - 1] == ["cactus", "terre", "terre", "terre", "terre", "terre"]:
        Map[taille_map - 1] = "terre"
    if Map_air[taille_map - 1] == ["oiseau"]:
        Map[taille_map - 1] = "terre"
    elif Map_air[taille_map - 2:taille_map - 1] == ["oiseau"]:
        Map[taille_map - 1] = "terre"
    elif Map_air[taille_map - 3:taille_map - 1] == ["oiseau", "air"]:
        Map[taille_map - 1] = "terre"
    elif Map_air[taille_map - 4:taille_map - 1] == ["oiseau", "air", "air"]:
        Map[taille_map - 1] = "terre"
    elif Map_air[taille_map - 5:taille_map - 1] == ["oiseau", "air", "air", "air"]:
        Map[taille_map - 1] = "terre"

def choix_terrain_air(Map_air):  # fonction contenant les regles de generation de la map air
    Map_air[taille_map - 1] = rdm.choice(entry_air)
    if Map[taille_map - 2:taille_map - 1] == ["cactus"]:
        Map_air[taille_map - 2] = "air"
    elif Map[taille_map - 3:taille_map - 1] == ["cactus","terre"]:
        Map_air[taille_map - 2] = "air"
    elif Map[taille_map - 4:taille_map - 1] == ["cactus", "terre", "terre"]:
        Map_air[taille_map - 2] = "air"
    elif Map[taille_map - 5:taille_map - 1] == ["cactus","terre", "terre", "terre"]:
        Map_air[taille_map - 2] = "air"
    if Map_air[taille_map - 2:taille_map - 1] == ["oiseau"]:
        Map_air[taille_map - 1] = "air"
    elif Map_air[taille_map - 3:taille_map - 1] == ["oiseau", "air"]:
        Map_air[taille_map - 1] = "air"
    elif Map_air[taille_map - 4:taille_map - 1] == ["oiseau", "air", "air"]:
        Map_air[taille_map - 1] = "air"
    elif Map_air[taille_map - 5:taille_map - 1] == ["oiseau", "air", "air", "air"]:
        Map_air[taille_map - 1] = "air"
    if Map[taille_map - 4:taille_map - 1] == ["cactus", "terre", "terre"]:
        Map_air[taille_map - 1] = "air"


def print_MAP(Map, Map_air,  posDino):  # covertisseur de texte en interface graphique
    s = ""
    x = ""
    for terrain in Map :
        if terrain == "R":
            s += "R"

        elif terrain == "terre":
            s += "_"
        elif terrain == "cactus":
            s += "8"

    for ciel in Map_air:
        if ciel == "oiseau" and terrain == "cactus":
            ciel = "air"
        if posDino >=1:
            Map_air[casedepart]= "°"
        else :
            Map_air[casedepart]= " "
        if ciel == "°":
            x += "°"
        if ciel == " ":
            x += " "

        elif ciel == "air":
            x += " "
        elif ciel == "oiseau":
            x += "-"


    print(x)
    print(s)



def saut(posDino): # refle verifiant
    if posDino == 0:
        return 5
    else:
        return posDino


# noinspection PyUnreachableCode
def GameOver(posDino, terrain, ciel ):
    if terrain == "cactus" and posDino == 0:
        return 0
    elif ciel == "oiseau" and posDino >= 1:
        return 0
    else:
        return 1






nombre_gene=10
taille_test=10
liste_test=[0]*taille_test
liste_poids=crea_liste_de_liste()
liste_poids_gene=premiers_poids()


#clock = pygame.time.Clock()
casedepart = 2
taille_map = 40  # defini la longueur de la map
stop = False  # bouléen pour stoper le programme
Map = ["terre"] * taille_map  # défini la map comme etant de la terre a t0
entry = ["cactus", "terre", "terre", "terre", "terre"]  # défini les possibilitées de spawn
Map_air = ["air"]* taille_map # la hauteur 1 est de l'air
entry_air = ["oiseau","air","air","air","air","air","air","air"] # spawns aériens

#pygame.display.set_caption('font example')
#size = [640, 480]
#screen = pygame.display.set_mode(size)
#basicfont = pygame.font.SysFont(None, 48)


#myfont = pygame.font.SysFont("monospace", 15)
#fenetre = pygame.display.set_mode((640, 480))
#vitesse = 600




for b in range (nombre_gene):
    
    for a in range(taille_test):
        Map = ["terre"] * taille_map
        poids_distance=liste_poids_gene[a][0]
        poids_largeur_cactus=liste_poids_gene[a][1]
        poids_distance2=liste_poids_gene[a][2]
        score = 0
        posDino = 0
        en_vie = 1
        continuer=1
        print(Map)
        while continuer:
            while not stop and en_vie:
                print_MAP ( Map, Map_air, posDino )
                distance=distance_next_cactus(Map)
                distance_bis=nonlin(distance)
                largeur_cactus=nb_cactus(Map,distance)
                distance2=distance_next_pigeon(Map_air)
                distance2_bis=nonlin(distance2)
                eventkey=choix_robot(Map)
                print('GENERATION', b+1)
                print('INDIVIDUAL',a+1)
                print(posDino)
                #print ('distance au cactus:', distance)
                #print ('distance a pigeon is:', distance2 )
                #print ('distance au cactus traitée:', distance2_bis)
                #print ('taille next obstacle is:', largeur_cactus)
                print ('facteur déterminant is', poids_distance*distance_bis + poids_largeur_cactus*largeur_cactus + poids_distance2*distance2_bis)
                # affichage de la map
                #pygame.event.pump()
                #keys = pygame.key.get_pressed()
                #pygame.time.delay(vitesse)
                #for event in pygame.event.get():
                #if event.type == KEYDOWN:   
                if eventkey == K_SPACE:
                            posDino = saut(posDino)
                if eventkey == K_ESCAPE:
                             choix = "stop"
                             stop = (choix == "stop")
                             continuer = 0
                if posDino >= 1:
                    posDino -= 1  # dino retombe
                en_vie = GameOver ( posDino , Map[ casedepart + 1 ] , Map_air[casedepart + 1 ] )
                for i in range ( taille_map - 1 ):
                    Map_air[ i ] = Map_air[ i + 1 ]
        
                    if posDino == 0:
                        Map_air[ casedepart ] = "P"
                    if Map_air[ casedepart ] == "P":
                        for i in range ( casedepart ):
                            Map_air[ i ] = "air"
                    else:
                        Map_air[ i ] = Map_air[ i + 1 ]  # décales toutes les entrées de la map vers la gauche
        
                for i in range ( taille_map - 1 ):
                    Map[ i ] = Map[ i + 1 ]
        
                    if posDino == 0:
                        Map[ casedepart ] = "R"
                    if Map[ casedepart ] == "R":
                        for i in range ( casedepart ):
                            Map[ i ] = "terre"
                    else:
                        Map[ i ] = Map[ i + 1 ]
                score += 1
                
        
                #chaine_map, chaine_ciel = print_MAP(Map , Map_air,  posDino)
                #text_map = basicfont.render(str(chaine_map), True, (0, 0,0), (255, 255, 255))
                #text_air = basicfont.render(str(chaine_ciel), True, (0, 0,0), (255, 255, 255))
                #textrect_air = text_air.get_rect()
                #textrect_map = text_map.get_rect()
                #textrect_air.centerx = screen.get_rect().centerx+20
                #textrect_air.centery = screen.get_rect().centery+25
                #textrect_map.centerx = screen.get_rect().centerx-130
                #textrect_map.centery = screen.get_rect().centery
                #screen.fill((255, 255, 255))
                #screen.blit(text_map, textrect_map)
                #screen.blit(text_air, textrect_air)
                #pygame.display.update()
                #clock.tick(20)
        
               # screen.fill((255, 255, 255))
               # screen.blit(text_map, textrect_map)
               # screen.blit(text_air, textrect_air)
        
                #pygame.display.update()
                #clock.tick(20)
                
                choix_terrain_air (Map_air)
                choix_terrain ( Map )
        
        
                #label = myfont.render("s", 1, (255,255,255))
                if en_vie == 0:
                    continuer = 0
                    
                #vitesse -= 3
                time.sleep(0.1)#delai pour plus de clartée
        #on stock les poids et le score de l'individu
        liste_poids[a]=[poids_distance,poids_largeur_cactus,poids_distance2]
        liste_test[a]=score
        print ( "Game Over" )
        print ( "vous avez scoré" , score , "!" )
        time.sleep(2)#delai pour plus de clartée
        
    
            
    print('             Resultats de la generation', b+1)    
    print(liste_test)
    print(liste_poids)
    print('the best scored:',max(liste_test))
    print('with weight:',liste_poids[indice_seaker()])
    i_1=indice_seaker()
    liste_test[i_1]=0
    print('the 2nd best scored',max(liste_test))
    i_2=indice_seaker()
    print('with weight:',liste_poids[i_2])
  
    
   

    if b!=nombre_gene-1:
        print('lets move to generation',b+2)
        croisement_genome()
        time.sleep(10) #delai pour plus de clartée

    
print('the end')
