# -*- coding: utf-8 -*-
from random import randint
"""
Created on Fri May  4 16:02:19 2018

@author: etudiant
"""

TDino = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
TMap = [0,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,0,1,0,1]
state = 0
NbCase = len(TMap)

def GenNewDino(TDino,state,NbCase):
    for i in range(state,NbCase):
        TDino[i]= randint(0,1)
        a = TDino[i]
        print(a)
    return(TDino)
        
def TestDino(TMap,TDino,Nbcase):
    state = 0
    for i in range(Nbcase):
        if TMap[i] == 1:
            if TDino[i] != 1:
                print("aie")
                state = i
                break
    return(state)
               
TDino = GenNewDino(TDino,state,NbCase)
state = TestDino(TMap,TDino,NbCase)

while state != 0:

    TDino = GenNewDino(TDino,state,NbCase)
    state = TestDino(TMap,TDino,NbCase)
    print(state)
    
print("Séquence trouvée!!!")
for i in range(NbCase):
    print(TDino[i])
