#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# printmatrix.py
#-----------------------

def printmatrix(matrix):
	for line in matrix:
            
		for element in line:
			print('%3d' % elem, end='')
		#fim for
			
		print()
		
	#end for
		
#end printMat
