# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:59:27 2021

@author: Bruker
"""
from sympy import diff, symbols, solve

r = symbols('r')

eps = 0.997 
sig = 3.40

V = 4*eps*((sig/r)**12-(sig/r)**6)

Fr = -diff(V, r)

V_r=V.subs(r, 4)
F_r = Fr.subs(r,4)

V_0 = solve(V, r)
F_0 = solve(Fr, r)


print('Når r=4.0 Å er potensialet V=', V_r,'kJ/mol og kraften F=', F_r,'N.') 
print('Potensialet er null når r=', V_0[1], 'Å og kraften er null når r=', F_0[1],'Å.')

