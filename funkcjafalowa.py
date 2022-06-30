# -*- coding: utf-8 -*-
"""
animacja funkcji falowej

Created on Thu Jun 30 13:38:08 2022

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
nx=2
ny=1
L = 1   # w tej wersji zakładamy, że Lx=Ly
x,y = np. linspace(0,L, 200), np. linspace(0,L,200)
A=(2/L)**0.5

def psi0(a,b):
    psi0=(  np.sin(( nx * np.pi * a)/L) * np.sin((ny * np.pi * b)/L))
    return psi0
X,Y = np.meshgrid(x,y)
psi_0 = np.array([psi0(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])

PSI_0 = psi_0.reshape(X.shape)  # wiecej wartosci!

fig2 = plt.figure()

ax2=fig2.add_subplot(111, projection = '3d')
ax2.plot_surface(X,Y,PSI_0, cmap = 'terrain')

plt.xlabel('X')
plt.ylabel('Y')
ax2.set_zlabel('Z')
plt.title(['Funkcja falowa dla Nx=%d i Ny=%d' % (nx,ny)], color= 'blue')
plt.savefig( ['Funkcja falowa dla Nx=%d i Ny=%d' % (nx,ny)], transparent = True)
