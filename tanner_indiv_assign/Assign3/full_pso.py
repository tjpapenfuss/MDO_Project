# Source for this: https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/


import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    "Objective function"
    return (1-x-y)*((np.sin(2*np.pi*x))**2 + (np.sin(2*np.pi*y))**2)


# Contour plot: With the global minimum showed as "X" on the plot
x, y = np.array(np.meshgrid(np.linspace(0,1,100), np.linspace(0,1,100)))
z = f(x, y)
x_min = x.ravel()[z.argmin()]
y_min = y.ravel()[z.argmin()]
plt.figure(figsize=(8,6))
plt.imshow(z, extent=[0, 1, 0, 1], origin='lower', cmap='viridis', alpha=0.5)
plt.colorbar()
plt.plot([x_min], [y_min], marker='x', markersize=5, color="white")
contours = plt.contour(x, y, z, 10, colors='black', alpha=0.4)
plt.clabel(contours, inline=True, fontsize=8, fmt="%.0f")


n_particles = 20
X = np.random.rand(2, n_particles) * 1
V = np.random.randn(2, n_particles) * 0.1
pbest = X
pbest_obj = f(X[0], X[1])
gbest = pbest[:, pbest_obj.argmin()]
gbest_obj = pbest_obj.min()
plt.plot(X, V)
# pbest_plot.set_offsets(pbest.T)
# p_plot.set_offsets(X.T)
# p_arrow.set_offsets(X.T)
# p_arrow.set_UVC(V[0], V[1])
# gbest_plot.set_offsets(gbest.reshape(1,-1))

plt.show()
