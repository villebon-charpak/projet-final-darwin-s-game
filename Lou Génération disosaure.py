# -*- coding: utf-8 -*-
from random import randint
"""
Created on Fri May  4 16:02:19 2018

@author: etudiant
"""

TDino = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
TMap = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1]

def GenDino():
    for i in range(20):
        TDino[i]= randint(0,1)
        a = TDino[i]
        print(a)
GenDino()

for i in range(20):
    if TMap[i] == 1:
        if TDino[i] != 1:
            print("aie")
            print(i)
            break