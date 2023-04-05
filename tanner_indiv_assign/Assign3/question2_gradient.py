import numpy as np
import numpy.linalg as la

import scipy.optimize as sopt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm

#import autograd.numpy as np  # Thinly-wrapped numpy
#from autograd import grad    # The only autograd function you may ever need

def f(x):
    return (1-x[0]-x[1])*((np.sin(2*np.pi*x[0]))**2 + (np.sin(2*np.pi*x[1]))**2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X, Y = np.meshgrid(np.linspace(0, 1, 20), np.linspace(0, 1, 20))
Z = f(np.array([X, Y]))
#print(fmesh)
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
# plt.axis("equal")
# plt.contour(X, Y, fmesh)
#plt.show()

# guesses = [np.array([0.7,0.7])]
# print(guesses)
# print("Starting gradient descent")
# x = guesses[-1]
# print(x)
# # Obtain its gradient function
def df(x):
    return np.array((-2*np.pi)*(x[0] + x[1] - 1)*(np.sin(4*np.pi*x[0])) - (np.sin(2*np.pi*x[0]))**2 - (np.sin(2*np.pi*x[1]))**2, 
            (-2*np.pi)*(x[0] + x[1] - 1)*np.sin(4*np.pi*x[1]) - (np.sin(2*np.pi*x[0]))**2 - (np.sin(2*np.pi*x[1]))**2)

# #grad_tanh = grad(f)
# #print(grad_tanh(x))
# # Search direction is steepest descent
# s = -df(x)

# def f1d(alpha):
#     return f(x + alpha*s)

# alpha_opt = sopt.golden(f1d)
# next_guess = x + alpha_opt * s
# guesses.append(next_guess)

# print(next_guess)
# https://towardsdatascience.com/implementing-the-steepest-descent-algorithm-in-python-from-scratch-d32da2906fe2
def steepest_descent(gradient, x0 = np.zeros(2), alpha = 0.01, max_iter = 10000, tolerance = 1e-10): 
    '''
    Steepest descent with constant step size alpha.
    
    Args:
      - gradient: gradient of the objective function
      - alpha: line search parameter (default: 0.01)
      - x0: initial guess for x_0 and x_1 (default values: zero) <numpy.ndarray>
      - max_iter: maximum number of iterations (default: 10000)
      - tolerance: minimum gradient magnitude at which the algorithm stops (default: 1e-10)
    
    Out:
      - results: <numpy.ndarray> of size (n_iter, 2) with x_0 and x_1 values at each iteration
    '''
    
    # Initialize the iteration counter
    iter_count = 1
    
    # Prepare list to store results at each iteration 
    results = np.array([])
    
    # Evaluate the gradient at the starting point 
    gradient_x = gradient(x0)
    
    # Set the initial point 
    x = x0 
    results = np.append(results, x, axis=0)
   
    # Iterate until the gradient is below the tolerance or maximum number of iterations is reached
    # Stopping criterion: inf norm of the gradient (max abs)
    while any(abs(gradient_x) > tolerance) and iter_count < max_iter:
        
        # Update the current point by moving in the direction of the negative gradient 
        x = x - alpha * gradient_x
        
        # Store the result
        results = np.append(results, x, axis=0)
        
        # Evaluate the gradient at the new point 
        gradient_x = gradient(x) 
        
        # Increment the iteration counter 
        iter_count += 1 
        
    # Return the points obtained at each iteration
    return results.reshape(-1, 2)

print(df(np.array([0.1, 0.1])))

estimate = steepest_descent(df, x0 = np.array([0.1, 0.1]), alpha=0.30)

print('Final results: {}'.format(estimate[-1]))
print('N° iterations: {}'.format(len(estimate)))