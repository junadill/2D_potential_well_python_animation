
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:26:01 2022

@author: justyna koper adam piwonski

Animacja gestosci prawdopodobienstwo
"""

import sympy as sp
from matplotlib import cm
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
sp.init_printing()


dt=0.001

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

psi_sim = sp.Function('psi')
psi_sim = 2/L * sp.sin(nx*sp.pi*x/L)*sp.sin(ny*sp.pi*y/L)
E = h**2 * sp.pi**2 * (nx**2 + ny**2)/(2*m*L**2)
PSI = psi_sim * sp.exp(-E*sp.I*t/h)
PSIF = lambdify((x,y,nx,ny,t),PSI.subs({h: 1, m: 1, L: 1}))


nx=2
ny=4

def update(i, z, line):
    t = i*dt
    z = np.abs(PSIF(xs,ys,nx,ny,t)/np.sqrt(2) + PSIF(xs,ys,nx,2*ny,t)/np.sqrt(2))**2
    ax.clear()
    line = ax.plot_surface(xs,ys,z,cmap=cm.autumn)
    ax.set_zlim(0, 5)
    return line,

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

xs = np.linspace(0, 1, 1000)
ys = np.linspace(0, 1, 1000)

xs,ys = np.meshgrid(xs,ys)
plt.close()
z = np.abs(PSIF(xs,ys,nx,ny,0)/np.sqrt(2) + PSIF(xs,ys,2*nx,2*ny,0)/np.sqrt(2))**2

line = ax.plot_surface(xs,ys,z,cmap=cm.coolwarm)

ax.set_zlim(0, 6)



figtitle_gestosc1 = 'kwadrat_modulu_ff_dla_Nx=%d' % (nx) 
figtitle_gestosc2 = '_i_Ny=%d' % (ny)
filename=figtitle_gestosc1 + figtitle_gestosc2 + ".gif"
print(filename)

animacja_kwadratu_modulu = FuncAnimation(
    fig, update, fargs=(z, line), interval=30, blit=False, save_count=200)


animacja_kwadratu_modulu.save(filename)




