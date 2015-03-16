#Nickson Santos Endlich
# -*- coding: utf-8 -*-
# createrandommatrix.py
#-----------------------

def createrandommatrix(lines, columns): 
    from random import randint
    #if you want other values, simply change the randint method parameters
    return [[randint(1,9) for j in range(columns)] for i in range(lines)]

#end createrandommatrix
