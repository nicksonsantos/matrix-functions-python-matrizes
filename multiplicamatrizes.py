#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# multiplicamatrizes.py
#-----------------------

def multiplicamatrizes(matrizA,matrizB): #se não atender os requisitos retornar None #devolve uma nova matriz
    numcolunas = len(matrizA[0])
    numlinhas = len(matrizB)
    if  numcolunas != numlinhas: #o numero de colunas de M deve ser igual ao numero de linhas de M
        return None
    else:
        novamatriz = []
        # ao analisar o problema eu entendi que a matriz resultante da multiplicação é
        #
        # [[linha 1A*coluna 1B, linha 1A*coluna 2B, ..., linha 1A*coluna N B]
        #  [linha 2A*coluna 1B, linha 2A*coluna 2B, ..., linha 2A*coluna N B]
        #  [.......*........, .......*........, ..., .......*........]
        #  [linhaN A*coluna 1B, linha 3A*coluna 2B, ..., linha 3A*coluna N B]]
        #
        # para nossa lógica, isso é a mesma coisa(ou mais facil) que:
        #
        # Bt = Matriz B transposta
        #
        # [[linha 1A*linha 1Bt, linha 1A*linha 2Bt, ..., linha 1A*linha N Bt]
        #  [linha 2A*linha 1Bt, linha 2A*linha 2Bt, ..., linha 2A*linha N Bt]
        #  [.......*........, .......*........, ..., .......*........]
        #  [linhaN A* linha 1Bt, linha 3A*linha 2Bt, ..., linha 3A*linha N Bt]]
         
