import numpy as np
# Importing PySwarms
from pyswarm import pso

lb = [0, 0]
ub = [1, 1]

def f(x):
    x1 = x[0]
    x2 = x[1]
    "Objective function"
    return -((1-x1-x2)*((np.sin(2*np.pi*x1))**2 + (np.sin(2*np.pi*x2))**2))

# Run the PSO algorithm
xopt, fopt = pso(f, lb, ub, swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-8,
    minfunc=1e-8, debug=False)

# Print the results of the optimization
print(xopt, fopt)

