#Nickson Santos Endlich
# transposed.py
#-----------------------

def transposed(matrix): #return a transposed matrix
     newmatrix = []
     numlines = len(matrix)
     
     for j in range(numcolumns): #browse through the columns of the matrix
          temporarylist = []
          
          for i in range(numlines): #browse through the lines of the matrix
               temporarylist.append(matrix[i][j])
               
          #end for
               
          newmatrix.append(temporarylist)
          
     #end for

     return newmatrix

#fim transposed

