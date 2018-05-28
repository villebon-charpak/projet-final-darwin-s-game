# UE Codage : projet informatique

## Description du projet

Créer un 'algorithme génétique' qui fonctionne par un mécanisme de génération 'd'objets' chacune apprenant des précédentes.

1ère idée: Battre un jeu d'obstacles aux actions simples, exemple du jeu 'raptor' de chrome , géométrie dash:
on ferait des générations de raptors/de cubes qui sautent aléatoirement et apprennent en quelque sorte le parcours.

## Composition de l'équipe

* membre 1 : Matthieu WAECKEL, responsable de : Trouver comment générer une map aléatoirement
* membre 2 : Lou VALLOGNES, responsable de : code du player // ordinateur
* membre 3 : Mickaël RENAUD, responsable de : recherche machine learning et application python


### mickael:

pour les versions bot:

-pour la version compatible interface graphique ('texte sur fenêtre pygame'), la fenêtre pygame freeze assez souvent mieux vaut ne pas l'ouvrir entièrement
-la version finale integre: 
--> un algorithme generationnel: on peut changer le nombre de generations et d'individus par generations,
les  generations sont en partie générées à partir des précédentes.
--> un recap des resultats de la generations, avec les 2 meilleurs individus, les poids associés etc... (fonctionnement cohérent et vérifié :) )
--> basé sur un système de reseaux neuronaux dont on peut changer le 'facteur déterminant' 
-la V2 n'est peut etre plus à jour (modif. non voulue fait qu'elle ne correspond plus à la V2 mais à une version entre V3 et finale)

ATTENTION: pour le moment seule la version finale (BOT VF) est en partie commentée pour ce qui concerne les blocks et fonctions 'bot': algo génétique // réseaux neuronaux 
la partie génération de map est elle en partie commentée dans tout les codes



