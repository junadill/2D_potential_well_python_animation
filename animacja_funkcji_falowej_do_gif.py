# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 08:22:26 2022
@author: justyna koper adam piwonski

Animacja funkcji falowej
"""

import sympy as sp
from matplotlib import cm
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
sp.init_printing()


x = sp.Symbol('x',real=True)
y = sp.Symbol('y', real=True)

h = sp.Symbol('hbar', integer=True, positive=True)
m = sp.Symbol('m', integer=True, positive=True)
L = sp.Symbol('L',real=True,positive=True)
ex = sp.Symbol('ex', real=True)
ey = sp.Symbol('ey', real=True)
N = sp.Symbol('N', real=True)
nx = sp.Symbol('nx', real=True,positive=True)
ny = sp.Symbol('ny', real=True,positive=True)
t = sp.Symbol('t',real=True, positive=True)
z = sp.Symbol('z',real=True)

psi_sim = sp.Function('psi')
psi_sim = 2/L * sp.sin(nx*sp.pi*x/L)*sp.sin(ny*sp.pi*y/L)
E = h**2 * sp.pi**2 * (nx**2 + ny**2)/(2*m*L**2)
PSI = psi_sim * sp.exp(-E*sp.I*t/h)
PSIF = lambdify((x,y,nx,ny,t),PSI.subs({h: 1, m: 1, L: 1})) #parametry jak na zajeciach Kwanty 2


nx=2
ny=4
dt=0.01

def update(i, z, line):
    t = i*dt
    z = PSIF(xs,ys,nx,ny,t)
    ax.clear()
    line = ax.plot_surface(xs,ys,z,cmap=cm.winter)
    ax.set_zlim(-2, 2)
    return line

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

xs = np.linspace(0, 1, 1000)
ys = np.linspace(0, 1, 1000)

xs,ys = np.meshgrid(xs,ys)
plt.close()
z = PSIF(xs,ys,nx,ny,0)

line = ax.plot_surface(xs,ys,z,cmap=cm.winter)

ax.set_zlim(-2, 2)



figtitle_ff1 = 'ff_dla_Nx=%d' % (nx) 
figtitle_ff2 = '_i_Ny=%d' % (ny)
filename=figtitle_ff1 + figtitle_ff2 + ".gif"
print(filename)

animacja_ff = FuncAnimation(
    fig, update, fargs=(z, line), interval=40, blit=False, save_count=150)


animacja_ff.save(filename)