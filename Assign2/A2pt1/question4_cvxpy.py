import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

x = cp.Variable(pos=True)
y = cp.Variable(pos=True)

a = cp.Parameter(neg=True)
b = cp.Parameter()

objective_fn = (x**2 + y**2)
objective = cp.Minimize(objective_fn)
constraints = [y == cp.power((x + a),(3/2))]
#constraints = [a*(x*y + x*z + y*z) <= b, x >= y**c]
problem = cp.Problem(objective, constraints)
#plt.plot(objective_fn)
print(np.pi)
print("problem is DCP:", problem.is_dcp())
print("problem is DGP:", problem.is_dgp())

# a.value = -1.0
# b.value = 0.0

# problem.solve(gp=True)
# print("status:", problem.status)
# print("optimal value", problem.value)

# print(x.value)
# print(y.value)
