
from scipy.optimize import minimize
from pyswarm import pso
import time as t


def fn(tuple):
    const = constraint(tuple)
    const = round(const, 3)
    #print(const)
    if(const != 0):
        return 1000*(const**2)
    else:
        return tuple[0]**2 - 0.0001*tuple[1]**2 + 1000*tuple[2]**2

def scaled_fn(tuple):
    const = constraint(tuple)
    const = round(const, 3)
    #print(const)
    if(const != 0):
        return 1000*(const**2)
    else:
        return tuple[0]**2 - tuple[1]**2 + tuple[2]**2

def constraint(tuple):
    return tuple[0]**2 + tuple[1]**2 + tuple[2]**2 - 1

cons = ({'type': 'eq', 'fun': lambda x:  x[0] + x[1] + x[2] - 1})

lb = [0,0,0]
ub = [5,5,5]
starttime = t.time()
lasttime = starttime
# Minimize objective function
experiment_tuple = (0,0,0)
result = minimize(fn, lb, ub, swarmsize=100, omega=0.5, phip=0.5, 
    phig=0.5, maxiter=1000, minstep=1e-8, minfunc=1e-8, debug=False)

print(result)

first_opt = round((t.time() - lasttime), 2)
middle_time = t.time()
print(first_opt)

scaled_result = pso(scaled_fn, lb, ub, swarmsize=100, omega=0.5, phip=0.5, 
    phig=0.5, maxiter=1000, minstep=1e-8, minfunc=1e-8, debug=False)

print(scaled_result)
second_opt = round((t.time() - middle_time), 2)
print(second_opt)