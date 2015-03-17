#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# zigzagA.py
#-----------------------



def zigzagA(matriz):
    numcolunas = len(matriz[0])
    numlinhas = len(matriz)
    from diagonalsecundaria import diagonalsecundaria
    lstpercurso = []
    matrizmenor = []
    numlinhas = len(matriz)
    limitematmenor = 1
    while limitematmenor <= numlinhas: #delimitamos as matrizes em matrizes menores e paramos na metade
        for i in range(limitematmenor):
            linha = []
            
            for j in range(limitematmenor):
            
                linha.append(matriz[i][j])
            #fim for
                
            matrizmenor.append(linha)    
        
        #fim for

        diagmatmenor = diagonalsecundaria(matrizmenor)
        
        if limitematmenor % 2 == 0:
            diagmatmenor.reverse()

        lstpercurso += diagmatmenor

        limitematmenor+=1
        matrizmenor = []
    
    #fim while   

    matrizmenor = []

    limitematmenor = 1
    
    while limitematmenor <= numlinhas:
        for i in range(limitematmenor, numlinhas):
            linha = []
            for j in range(limitematmenor, numcolunas):
                linha.append(matriz[i][j])
            #fim for
            matrizmenor.append(linha)
        #fim for

        diagmatmenor = diagonalsecundaria(matrizmenor)

        if (limitematmenor % 2) == 0:
            diagmatmenor.reverse()

        lstpercurso += diagmatmenor

        limitematmenor+=1
        matrizmenor = []                            

    return lstpercurso
    

def main():
    from random import randint
    from printmatriz import printmatriz
    matriz = [[randint(1,9) for j in range(50)] for i in range(50)]
    printmatriz(matriz)
    print(zigzagA(matriz))
#fim main

if __name__ == '__main__':
	main()
