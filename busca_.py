# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import random

def objfun (x):
    return va * x**2 + vb*x + vc
    
va = 1
vb = -5
vc = 30

xmin = -100
xmax = 100

qtd_pontos = 50

passo = (xmax - xmin) / (qtd_pontos-1)
vet = [xmin]
for i in range(1, qtd_pontos):
    vet.append (vet[-1]+passo)

minx=-vb/2*va
delta = (-vb)**2 - 4*va*vc
miny = -delta/4*va

plt.cla()
plt.clf()
plt.plot (vet, fx, "b")
plt.plot (minx, miny, "g", marker = "x", markersize = 12, linewidth = 10, markeredgewidth = 2)
plt.ylabel('y=f(x)')
plt.xlabel('x')
plt.draw()
plt.show()



fx = [ objfun(x) for x in vet ]

plt.clf()
plt.plot(vet, fx, "b")