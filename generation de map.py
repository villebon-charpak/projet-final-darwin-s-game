# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:29:32 2018

@author: MATTHIEU 
"""
import pygame
import random as rdm
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
casedepart = 2
score = 2
posDino = 0
en_vie = 1
taille_map = 40  # defini la longueur de la map
stop = False  # bouléen pour stoper le programme
boucle = 1  # variable du while permettant de le break
Map = ["terre"] * taille_map  # défini la map comme etant de la terre a t0
entry = ["cactus", "terre", "terre", "terre", "terre"]  # défini les possibilitées de spawn
Map_air = ["air"]* taille_map # la hauteur 1 est de l'air
entry_air = ["oiseau","air","air","air","air","air","air","air"] # spawns aériens

pygame.display.set_caption('font example')
size = [640, 480]
screen = pygame.display.set_mode(size)
basicfont = pygame.font.SysFont(None, 48)





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


    return x,s



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
        print_MAP ( Map, Map_air, posDino )  # affichage de la map
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
        score *= 1.005

        chaine_map, chaine_ciel = print_MAP(Map , Map_air,  posDino)
        text_map = basicfont.render(str(chaine_map), True, (0, 0,0), (255, 255, 255))
        text_air = basicfont.render(str(chaine_ciel), True, (0, 0,0), (255, 255, 255))
        textrect_air = text_air.get_rect()
        textrect_map = text_map.get_rect()
        textrect_air.centerx = screen.get_rect().centerx+20
        textrect_air.centery = screen.get_rect().centery+25
        textrect_map.centerx = screen.get_rect().centerx-130
        textrect_map.centery = screen.get_rect().centery

        screen.fill((255, 255, 255))
        screen.blit(text_map, textrect_map)
        screen.blit(text_air, textrect_air)

        pygame.display.update()
        clock.tick(20)
        choix_terrain_air (Map_air)
        choix_terrain ( Map )


        label = myfont.render("s", 1, (255,255,255))
        if en_vie == 0:
            continuer = 0
            break
        vitesse -= 3



print ( "Game Over" )
print ( "vous avez scoré" , score , "!" )
