# -*- coding: utf-8 -*-
from random import randint
"""
Created on Fri May  4 16:02:19 2018

@author: etudiant
"""
x = 0
win = 0

TDino = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1]
TMap = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1]

Nbcase = len(TMap)
"""def GenNewDino(TDino,x):
    for i in range(x,20):
        TDino[i]= randint(0,1)
        a = TDino[i]
        print(a)
    return(TDino)"""
        
def TestDino1(TMap,TDino,Nbcase):
    for i in range(Nbcase):
        if TMap[i] == 1:
            if TDino[i] != 1:
                print("aie")
                return(i)
    if x == 0:
        return(0)

win = TestDino1(TMap,TDino,Nbcase)
print(win)
                


"""while win==0:

    TDino = GenNewDino(TDino,x)
    TestDino1()"""





