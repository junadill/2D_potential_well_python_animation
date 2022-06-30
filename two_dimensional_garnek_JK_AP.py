# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:26:01 2022

@author: justyna koper adam piwonski
"""

import sympy as sp
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
from IPython.display import HTML
sp.init_printing()

n=5
L = 1** -10 
x,y = np. linspace(0,L, 200), np. linspace(0,L,200)
A=(2/L)**0.5


def psi(a,b):
    psi=(  np.sin(( n * np.pi * a)/L) * np.sin((n * np.pi * b)/L))**2
    return psi

X,Y = np.meshgrid(x,y)

psi1 = np.array([psi(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])

PSI = psi1.reshape(X.shape)  # wiecej wartosci!


###
fig = plt.figure()

ax=fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,PSI, cmap = 'winter')

plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.title(['Gestosc prawdopodobienstwa dla n=%d' % (n)], color= 'red')
plt.savefig( ['Gestosc prawdopodobienstwa n=%d.png' % (n)], transparent = True)