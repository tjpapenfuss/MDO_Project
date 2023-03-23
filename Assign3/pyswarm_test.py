# Import all the modules
import numpy as np
# Importing PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Designer
from pyswarms.utils.plotters.formatters import Mesher

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
# Perform optimization
cost, pos = optimizer.optimize(fx.sphere, iters=1000)

m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0,0))

# f = r"./animation.mp4" 
# writervideo = animation.FFMpegWriter(fps=60) 
# animation.save(f, writer=writervideo) 
animation.save('animation.mp4')

#Code for 3D Plot :
# The preprocessing
pos_history_3d = m.compute_history_3d(optimizer.pos_history)
# Adjusting the figure
d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])
animation3d = plot_surface(pos_history=pos_history_3d, # The cost_history that we computed
                           mesher=m, designer=d,       # Various Customizations
                           mark=(0,0,0))               # Mark the minima

# f = r"./sphere.mp4" 
# writervideo = animation.FFMpegWriter(fps=60) 
# animation.save(f, writer=writervideo) 

animation3d.save('sphere.mp4')
