# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:29:32 2018

@author: MATTHIEU 
"""
import pygame
import random as rdm
from pygame.locals import *
pygame.init()

casedepart = 2
score = 2
posDino = 0
en_vie = 1
taille_map = 40  # defini la longueur de la map
stop = False  # bouléen pour stoper le programme
boucle = 1  # variable du while permettant de le break
Map = ["terre"] * taille_map  # défini la map comme etant de la terre a t0
entry = ["cactus", "terre", "terre", "terre", "terre"]  # défini les possibilitées de spawn

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


def print_MAP(liste, posDino):  # covertisseur de texte en interface graphique
    s = ""
    for terrain in liste:
        if terrain == "R":
            s += "R"

        elif terrain == "terre":
            s += "_"
        elif terrain == "cactus":
            s += "8"
    if posDino == 0:
        print("")
    else:
        print(" " * casedepart + "°")
    print(s)


def saut(posDino):
    if posDino == 0:
        return 5
    else:
        return posDino


def GameOver(posDino, terrain):
    if terrain == "cactus" and posDino == 0:
        return 0
    else:
        return 1


continuer = 1
myfont = pygame.font.SysFont("monospace", 15)
fenetre = pygame.display.set_mode((640, 480))
vitesse = 600

print(Map)   # affichage de la map a t 0

while continuer:
    while not stop and en_vie:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        pygame.time.delay(vitesse)
        print_MAP ( Map , posDino )  # affichage de la map
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    posDino = saut(posDino)
                if event.key == K_ESCAPE:
                     choix = "stop"
                     stop = (choix == "stop")
                     continuer = 0
        if posDino >= 1:
            posDino -= 1  # dino retombe
        en_vie = GameOver ( posDino , Map[ casedepart + 1 ] )
        for i in range ( taille_map - 1 ):
            Map[ i ] = Map[ i + 1 ]

            if posDino == 0:
                Map[ casedepart ] = "R"
            if Map[ casedepart ] == "R":
                for i in range ( casedepart ):
                    Map[ i ] = "terre"
            else:
                Map[ i ] = Map[ i + 1 ]  # décales toutes les entrées de la map vers la gauche
        score += 10
        score *= 1.885
        score /= 1.803
       
        choix_terrain ( Map )
        label = myfont.render("s", 1, (255,255,255))
        if en_vie == 0:
            continuer = 0
            break
        vitesse -= 2



print ( "Game Over" )
print ( "vous avez scoré" , score , "!" )
