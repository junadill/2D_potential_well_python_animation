# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:26:01 2022

@author: justyna koper adam piwonski
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
sp.init_printing()

sx = sp.Symbol('x', real = True)
sk = sp.Symbol('k', real = True, positive = True)
sa = sp.Symbol('a', real = True, positive = True)
sA = sp.Symbol('A', real = True, positive = True)
sn = sp.Symbol('n', integer = True, positive = True)
spsi = sp.Function('psi')
sx, sk, spsi(sx), sa