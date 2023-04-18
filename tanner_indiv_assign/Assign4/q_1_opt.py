
from scipy.optimize import minimize
from pyswarm import pso
import time as t


def fn(tuple):
    const = constraint(tuple)
    const = round(const, 3)
    #print(const)

    return tuple[0]**2 - 0.0001*tuple[1]**2 + 1000*tuple[2]**2

def scaled_fn(tuple):
    const = constraint(tuple)
    const = round(const, 3)
    #print(const)
    return tuple[0]**2 - tuple[1]**2 + tuple[2]**2

def constraint(tuple):
    return tuple[0]**2 + tuple[1]**2 + tuple[2]**2 - 1

cons = ({'type': 'eq', 'fun': lambda x:  x[0]**2 + x[1]**2 + x[2]**2 - 1})

x0_bnds = (-5,5)
x1_bnds = (-5,5)
x2_bnds = (-5,5)

starttime = t.time()
lasttime = starttime
# Minimize objective function
experiment_tuple = (0,0,0)
bnds = (x0_bnds, x1_bnds, x2_bnds)
result = minimize(fun=fn, x0=experiment_tuple, method='SLSQP', bounds=bnds, constraints=cons)

print(result)

first_opt = round((t.time() - lasttime), 2)
middle_time = t.time()
print(first_opt)

scaled_result = minimize(fun=scaled_fn, x0=experiment_tuple, method='SLSQP', bounds=bnds, constraints=cons)


print(scaled_result)
second_opt = round((t.time() - middle_time), 2)
print(second_opt)