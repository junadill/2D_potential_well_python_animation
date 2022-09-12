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
from IPython.display import HTML
sp.init_printing()
x = sp.Symbol('x',real=True)
y = sp.Symbol('y', real=True)

h = sp.Symbol('hbar', integer=True, positive=True)
m = sp.Symbol('m', integer=True, positive=True)
t = sp.Symbol('t',real=True, positive=True)


nx=1
ny=1
L = 1   # w tej wersji zakładamy, że Lx=Ly


x,y = np. linspace(0,L, 200), np. linspace(0,L,200)
A=(2/L)**0.5

def psi0(a,b):  #funkcja falowa
    psi0=(  np.sin(( nx * np.pi * a)/L) * np.sin((ny * np.pi * b)/L))
    return psi0

X,Y = np.meshgrid(x,y)
psi_0 = np.array([psi0(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])

#PSI_0 = psi_0.reshape(X.shape)  # wiecej wartosci!

#fig2 = plt.figure()

#ax2=fig2.add_subplot(111, projection = '3d')
#ax2.plot_surface(X,Y,PSI_0, cmap = 'terrain')

#plt.xlabel('X')
#plt.ylabel('Y')
#ax2.set_zlabel('Z')
#plt.title(['Funkcja falowa dla Nx=%d i Ny=%d' % (nx,ny)], color= 'blue')
#plt.savefig( ['Funkcja falowa dla Nx=%d i Ny=%d' % (nx,ny)], transparent = True)

####teraz zależne od czasu

#wzór na energię
E = h**2 * sp.pi**2 * (nx**2 + ny**2)/(2*m*L**2)
# psi(t)
fpom=sp.exp(-E*sp.I*t/h)
PSI_t= psi_0*fpom
PSIF = lambdify((x,y,nx,ny,t)),PSI_t.subs({h: 1, m: 1 })

dt = 0.001
n1 = 3
n2 = 2

def update(i, z, line):
    t = i*dt
    z = PSIF(xs,ys,n1,n2,t)
    ax.clear()
    line = ax.plot_surface(xs,ys,z,cmap="autumn")
    ax.set_zlim(-1.5, 1.5)
    return line,

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

xs = np.linspace(0, 1, 1000)
ys = np.linspace(0, 1, 1000)

xs,ys = np.meshgrid(xs,ys)
plt.close()
z = PSIF(xs,ys,n1,n2,0)

line = ax.plot_surface(xs,ys,z,cmap="autumn")

ax.set_zlim(-1.5, 1.5)