import numpy as np
# Importing PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Designer
from pyswarms.utils.plotters.formatters import Mesher

def f(x):
    x1 = x[0]
    x2 = x[1]
    "Objective function"
    return ((1-x1-x2)*((np.sin(2*np.pi*x1))**2 + (np.sin(2*np.pi*x2))**2))

# lower and upper bound
lb = [0,0]
ub = [1,1]
# xopt, fopt = ps(f, lb, ub)
# print(xopt, fopt)
# Contour plot: With the global minimum showed as "X" on the plot
# Set-up hyperparameters
max_bound = np.ones(2)
min_bound = 0 * max_bound
bounds = (min_bound, max_bound)
#print(np.ones(2))
print(max_bound)
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# Call instance of PSO
# x, y = np.array(np.meshgrid(np.linspace(0,1,100), np.linspace(0,1,100)))
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options, bounds=bounds)
# Perform optimization
# z = f(x,y)
cost, pos = optimizer.optimize(f, 1000, 1, 1)

m = Mesher(func=f)
animation = plot_contour(pos_history=optimizer.pos_history,
                        mesher=m,
                        mark=(0,0))

# f = r"./animation.mp4" 
# writervideo = animation.FFMpegWriter(fps=60) 
# animation.save(f, writer=writervideo) 
animation.save('animation.mp4')

# #Code for 3D Plot :
# # The preprocessing
# pos_history_3d = m.compute_history_3d(optimizer.pos_history)
# # Adjusting the figure
# d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])

# animation3d = plot_surface(pos_history=pos_history_3d, # The cost_history that we computed
#                            mesher=m, designer=d,       # Various Customizations
#                            mark=(0,0,0))               # Mark the minima

# # f = r"./sphere.mp4" 
# # writervideo = animation.FFMpegWriter(fps=60) 
# # animation.save(f, writer=writervideo) 

# animation3d.save('sphere.mp4')
