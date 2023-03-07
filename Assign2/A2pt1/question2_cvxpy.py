import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

x = cp.Variable(pos=True)
y = cp.Variable(pos=True)

V = cp.Parameter(pos=True)

objective_fn = ((2 * np.pi) * x * (x+y))
objective = cp.Minimize(objective_fn)
constraints = [(y == V/(np.pi*(x**2)))]
#constraints = [((np.pi * (x**2) * y) - V == b)]
#constraints = [a*(x*y + x*z + y*z) <= b, x >= y**c]
problem = cp.Problem(objective, constraints)
#plt.plot(objective_fn)
#print(np.pi)
print("problem is DCP:", problem.is_dcp())
print("problem is DGP:", problem.is_dgp())

#print(problem.is_dgp(dpp=True))
V.value = 1000.0
#b.value = 0.0
problem.solve(gp=True)
print("status:", problem.status)
print("optimal value", problem.value)

print(x.value)
print(y.value)
