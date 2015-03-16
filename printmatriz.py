#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# printmatriz.py
#-----------------------

def printmatriz(matriz):
	for linha in matriz:
            
		for elemento in linha:
			print('%3d' % elemento, end='')
		#fim for
			
		print()
		
	#fim for
		
#fim printMat
