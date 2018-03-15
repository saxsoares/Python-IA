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
print(vet)

fx = [ objfun(x) for x in vet ]

plt.clf()
plt.plot(vet, fx, "b")