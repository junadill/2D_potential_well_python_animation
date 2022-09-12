# -*- coding: utf-8 -*-
"""
animacja kwadratu modułu funkcji falowej

Created on Thu Jun 30 13:44:32 2022

@author: justyna koper adam piwonski
"""
import sympy as sp
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


sp.init_printing()
nx=3
ny=2
L = 1 # w tej wersji zakładamy, że Lx=Ly
x,y = np. linspace(0,L, 200), np. linspace(0,L,200)
A=(2/L)**0.5
def psi(a,b):
    psi=(  np.sin(( nx * np.pi * a)/L) * np.sin((ny * np.pi * b)/L))**2
    return psi

X,Y = np.meshgrid(x,y)

psi1 = np.array([psi(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])
#
PSI = psi1.reshape(X.shape)  # wiecej wartosci!


###
fig = plt.figure()

ax=fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,PSI, cmap = 'autumn')

plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')

figtitle = 'Gestosc prawdopodobienstwa dla Nx=%d i Ny=%d' % (nx,ny)

plt.title(figtitle, color= 'orange')
plt.savefig( figtitle, transparent = True)

plt.close()
####