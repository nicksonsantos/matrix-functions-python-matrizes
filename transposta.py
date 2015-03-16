#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# transposta.py
#-----------------------

def transposta(matriz): #retorna uma matriz transposta
     novamatriz = []
     numcolunas = len(matriz[0])
     numlinhas = len(matriz)

     for j in range(numcolunas): #navega atraves das colunas da matriz
          listatemporaria = []
          
          for i in range(numlinhas): #navega atraves das linhas da matriz
               listatemporaria.append(matriz[i][j])
               
          #end for
               
          novamatriz.append(listatemporaria)
          
     #end for

     return novamatriz

#fim transposed
