#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# diagonalsecundaria.py
#-----------------------

def diagonalsecundaria(matriz):
    lstdiag = []
    tamanhomatriz= len(matriz)
    i = tamanhomatriz - 1#posicao da linha
    j = 0 #posicao da coluna
    while i >= 0:
        lstdiag.append(matriz[i][j])
        i-= 1
        j+= 1
    #fim while

    return lstdiag

#fim diagonalSecundaria

