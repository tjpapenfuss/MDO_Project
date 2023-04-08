import numpy as np
# Importing PySwarms
# import pyswarms as ps
# import pyswarms.backend as P
# from pyswarms.backend.topology import Star
# from pyswarms.utils.functions import single_obj as fx
# import matplotlib.pyplot as plt
# from pyswarms.utils.plotters import plot_contour, plot_surface
# from pyswarms.utils.plotters.formatters import Designer
# from pyswarms.utils.plotters.formatters import Mesher

from pyswarm import pso

lb = [0, 0]
ub = [1, 1]

def f(x):
    x1 = x[0]
    x2 = x[1]
    "Objective function"
    return -((1-x1-x2)*((np.sin(2*np.pi*x1))**2 + (np.sin(2*np.pi*x2))**2))

xopt, fopt = pso(f, lb, ub, swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-8,
    minfunc=1e-8, debug=False)
print(xopt, fopt)

# lower and upper bound
# lb = [0,0]
# ub = [1,1]
# xopt, fopt = ps(f, lb, ub)
# print(xopt, fopt)
# Contour plot: With the global minimum showed as "X" on the plot
# Set-up hyperparameters
# max_bound = np.ones(2)
# min_bound = 0 * max_bound
# bounds = (min_bound, max_bound)
# #print(np.ones(2))
# print(max_bound)
# from pyswarms.single import GlobalBestPSO

# my_options = {'c1': 0.6, 'c2': 0.3, 'w': 0.4} # arbitrarily set
# #my_swarm = P.create_swarm(n_particles=10, dimensions=1, options=my_options, bounds=bounds) # The Swarm Class
# optimizer = GlobalBestPSO(n_particles=10, dimensions=2, options=my_options, bounds=bounds) # Reuse our previous options
# optimizer.optimize(f, print_step=100, iters=100, verbose=3)

