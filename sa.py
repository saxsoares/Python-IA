# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import random

def objfun (x):
    return 10 * math.sin( 0.3*x) * \
    math.sin(1.3*x**2) + \
    0.00001 * x**4 + 0.2*x + 80
    
xmin = -50
xmax = 50

qtd_pontos = 1000

passo = (xmax - xmin) / float(qtd_pontos-1)
vet = [xmin]
for i in range(1, qtd_pontos+1):
    vet.append (vet[-1]+passo)
print(vet)

fx = [ objfun(x) for x in vet ]

plt.clf()
plt.plot(vet, fx, "b")
plt.plot(minx, miny, "g", marker="x",
         markersize=12, linewidth=10, 
         markeredgewidth=3)