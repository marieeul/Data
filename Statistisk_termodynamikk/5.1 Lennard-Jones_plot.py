from sympy import symbols, plot

r = symbols('r')

eps = 1 #Fill in a value for epsilon
sig = 1 #Fill in a value for sigma

V = 4*eps*((sig/r)**12-(sig/r)**6) #Fill in a value for Lennard-Jones potential
# V=4*eps*(r/2-sig)

y_min = -eps
y_maks = 4*eps

plot(V, (r, 0.0001, 10), xlabel='Radial distance', ylabel='Potential', axis_center=(0,0), ylim=(y_min,y_maks))