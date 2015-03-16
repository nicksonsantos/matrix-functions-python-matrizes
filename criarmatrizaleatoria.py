#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# criarmatrizaleatoria.py
#-----------------------

def criarmatrizaleatoria(linhas, colunas): 
    from random import randint
    #se voce quiser outros valores, simplesmente mude os parametros da funcao randit
    return [[randint(1,9) for j in range(colunas)] for i in range(linhas)]

#end criarmatrizaleatoria
