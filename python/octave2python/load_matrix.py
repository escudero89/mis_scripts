import numpy as np
import matplotlib.pyplot as plt

# Transposing a List of Lists with Different Lengths
# source: http://code.activestate.com/recipes/410687-transposing-a-list-of-lists-with-different-lengths/

def transposed(lists):
   if not lists: return []
   return map(lambda *row: list(row), *lists)

#####
## Basicamente, agarra una matriz con posiciones de puntos en un espacio 2d (xi, yi), y los plotea
## entre unos limites.

## Le paso el nombre de la matriz.dat, donde los voy a guardar, los limites de los ejes,
## y si hay uniones entre puntos (el primer punto es el 1)
## Ej: arrows = [[1 2][1 3]] me une a la particula 1 con dos y con tres mediante lineas.

## @@TODO: Generalizarlo mas.
####

def matrix2png(matrixname, savedfolder, xlim, ylim, arrows):
    matrix = open(matrixname, 'r').readlines()
    matrix = [i.split() for i in matrix]
    matrix = [[float(j) for j in i] for i in matrix]

    matrix_t = transposed(matrix)

    y = []

    for col in range(0,len(matrix_t)):
        y.append(matrix_t[col])

    longitud = len(y)

    for i in range(0, len(y[1])):
        for j in range(0, longitud/2):                    
            plt.plot(y[j*2][i],y[j*2+1][i],'o')
        
        for a in arrows:
            ao = a[0] - 1
            ai = a[1] - 1
            plt.arrow(y[ao*2][i], y[ao*2+1][i], y[ai*2][i]-y[ao*2][i],y[ai*2+1][i]-y[ao*2+1][i])        

        #Limites de los ejes
        plt.xlim(xlim[0], xlim[1])
        plt.ylim(ylim[0], ylim[1])
        plt.savefig(savedfolder + str(i).zfill(5) + '.png')
        plt.clf()
        
    plt.close()

matrix2png('map.dat', 'temp/', [0, 12], [-4, 8], [[1, 3], [1, 2], [1, 5], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]])
