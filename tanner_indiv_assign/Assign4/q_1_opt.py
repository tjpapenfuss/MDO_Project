from scipy.optimize import minimize
from pyswarm import pso
import time as t

def fn(tuple):
    return tuple[0]**2 - 0.001*tuple[1]**2 + 1000*tuple[2]**2

def scaled_fn(tuple):
    return tuple[0]**2 - tuple[1]**2 + tuple[2]**2

def constraint(tuple):
    return tuple[0]**2 + tuple[1]**2 + tuple[2]**2 - 1

cons = ({'type': 'eq', 'fun': lambda x:  x[0]**2 + x[1]**2 + x[2]**2 - 1})
cons_scaled = ({'type': 'eq', 'fun': lambda x:  x[0]**2 + (1000*(x[1]**2)) + (0.001*(x[2]**2)) - 1})

starttime = t.time()
lasttime = starttime
# Minimize objective function
experiment_tuple = (0,0,0)
experiment_tuple_scaled = (0,0,0)
# bnds = (x0_bnds, x1_bnds, x2_bnds)
result = minimize(fun=fn, x0=experiment_tuple, method='SLSQP', constraints=cons)
first_opt = round((t.time() - lasttime), 6)

print("Initial optimization with the unscaled function.")
print(result)
print("Time for the first minimization: " + str(first_opt))

middle_time = t.time()
scaled_result = minimize(fun=scaled_fn, x0=experiment_tuple_scaled, method='SLSQP', constraints=cons_scaled)
second_opt = round((t.time() - middle_time), 6)

print("Second optimization with the scaled function.")
print(scaled_result)
print("Time for the scaled minimization: " + str(second_opt))
final_arr = scaled_result.x * [1, 31.62, 0.03162]
print("The final optimized point is: x1 = " + str(round(final_arr[0], 3)) + ", x2 = " 
    + str(round(final_arr[1], 3)) + ", x3 = "+ str(round(final_arr[2], 3)))

