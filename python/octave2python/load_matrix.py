import numpy as np
import matplotlib.pyplot as plt

# Transposing a List of Lists with Different Lengths
# source: http://code.activestate.com/recipes/410687-transposing-a-list-of-lists-with-different-lengths/

def transposed(lists):
   if not lists: return []
   return map(lambda *row: list(row), *lists)

#####

def matrix2png(matrixname, savedfolder):
    matrix = open(matrixname, 'r').readlines()
    matrix = [i.split() for i in matrix]
    matrix = [[float(j) for j in i] for i in matrix]

    matrix_t = transposed(matrix)

    y = []

    for col in range(0,len(matrix_t)):
        y.append(matrix_t[col])

    longitud = len(y)

    # Particulas comienzan en 1. 
    arrows = [[1, 3], [1, 2], [1, 5], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]]

    for i in range(0, len(y[1])):
        for j in range(0, longitud/2):                    
            plt.plot(y[j*2][i],y[j*2+1][i],'o')
        
        for a in arrows:
            ao = a[0] - 1
            ai = a[1] - 1
            plt.arrow(y[ao*2][i], y[ao*2+1][i], y[ai*2][i]-y[ao*2][i],y[ai*2+1][i]-y[ao*2+1][i])        

        #Limites de los ejes
        plt.xlim(0, 12)
        plt.ylim(-4, 8)
        plt.savefig(savedfolder + str(i).zfill(4) + '.png')
        plt.clf()
        
    plt.close()

matrix2png('map.dat', 'temp/')
