import nlopt
from numpy import *
import numpy as np


def myfunc(x, grad):
    if grad.size > 0:
        grad[0] = 4*np.pi*(x[0]) + 2*np.pi*(x[1])
        grad[1] = 2*np.pi*(x[0])
    return (2*np.pi*((x[0])**2) + 2*np.pi*(x[0])*(x[1]))

def myconstraint(x, grad, V):
    if grad.size > 0:
        grad[0] = 2 * np.pi * (x[0]) * (x[1])
        grad[1] = np.pi * ((x[0])**2)
    return np.pi * ((x[0])**2) * (x[1]) - V

opt = nlopt.opt(nlopt.LD_MMA, 1)
opt.set_lower_bounds([-float('inf'), 0])
opt.set_min_objective(myfunc)
opt.add_equality_constraint(lambda x,grad: myconstraint(x,grad,1000), 1e-8)
#opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
opt.set_xtol_rel(1e-4)
x = opt.optimize([3.123, 6.123])
minf = opt.last_optimum_value()

print("optimum at ", x[0], x[1])
print("minimum value = ", minf)
print("result code = ", opt.last_optimize_result())