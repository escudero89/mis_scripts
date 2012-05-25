#!/usr/bin/env python

import math, sys
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Arc, Circle
import matplotlib.lines as lines

def main(sigma_x, sigma_y, sigma_xy):
    
    # Variables iniciales
    
    escala = 1
    borde = 1
    '''
    sigma_x = 0
    sigma_y = 0
    sigma_xy = 8      
    '''
    OC = float(sigma_x + sigma_y) / 2
    radio = math.sqrt(pow(float(sigma_x - sigma_y)/2, 2) + sigma_xy * sigma_xy)
    
    # Retorna alfa en radianes, asi que lo pasamos a grados, e invertimos su signo
    if (sigma_xy == 0):
        alfa = math.pi
    else:
        alfa = math.acos((sigma_x - sigma_y) / (2 * radio)) / 2
        alfa = -alfa / math.pi * 180    
    
    # Variables para plotear
    
    ancho = int( (abs(radio) + abs(OC)) * 2 * escala + borde * 2 )
    alto = int( abs(radio) * 2 * escala + borde * 2 )
    paso = 10      
    
    delta_x = ancho / 2
    delta_y = alto / 2

    # Puntos
    
    A = { "x" : sigma_x, "y" : -sigma_xy }
    B = { "x" : sigma_y, "y" : sigma_xy }
    C = { "x" : OC, "y": 0 }
      
    # Preparo para plotear
    
    p0 = [-delta_x + OC, -delta_y * 2]
    p1 = [delta_x + OC, delta_y * 2]
          
    fig = plt.figure()    
    ax1 = fig.add_subplot(111)

    # Agrego figuras
       
    ax1.plot(A["x"], A["y"], 'o', label="A")
    ax1.plot(B["x"], B["y"], 'o', label="B")
    ax1.plot(C["x"], C["y"], 'o', label="C")   
           
    ax1.add_line(lines.Line2D((-ancho, ancho),(0, 0), linewidth=1, color="black"))
    ax1.add_line(lines.Line2D((0, 0),(-alto, alto), linewidth=1, color="black"))    

    ax1.add_line(lines.Line2D((A["x"],B["x"]),(A["y"],B["y"]),
        linewidth=1,
        color="red"))

    ax1.add_artist(Circle((C["x"], C["y"]), radio, fill=False, color="blue"))

    arc_len = radio
    ax1.add_artist(Arc((C["x"], C["y"]), 
        arc_len, arc_len, 
        theta1=alfa*2,
        theta2=0,
        color="purple",
        label="2 alfa = " + str(alfa)))
        

    plt.annotate('A', xy=(A["x"]+.5, A["y"]+.5), size='large')
    plt.annotate('B', xy=(B["x"]+.5, B["y"]+.5), size='large')
    plt.annotate('C', xy=(C["x"]+.5, C["y"]+.5), size='large')        
    
    plt.annotate(str(round(alfa*2, 2)), 
        xy=(C["x"]+arc_len/2, C["y"]-arc_len/2), 
        color="purple", 
        size='large')
    
    # Ploteo
    
    ax1.grid(True)
    ax1.axis('equal')
    ax1.axis((p0[0], p1[0], p0[1], p1[1]))

    plt.show()
    
if __name__ == "__main__":

    sigma_x = int(sys.argv[1])
    sigma_y = int(sys.argv[2])
    sigma_xy = int(sys.argv[3])

    sys.exit(main(sigma_x, sigma_y, sigma_xy))
