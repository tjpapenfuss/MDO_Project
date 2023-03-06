import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)


objective_fn = ((2 * np.pi) * x * (x+y))
objective = cp.Minimize(objective_fn)
constraints = [(np.pi * (x**2) * y) - 1000 == 0, x>=0, y>=0]
#constraints = [a*(x*y + x*z + y*z) <= b, x >= y**c]
problem = cp.Problem(objective, constraints)
#plt.plot(objective_fn)
print(np.pi)
#print(problem.is_dgp(dpp=True))

problem.solve(solver='GLPK_MI')
print("status:", problem.status)
print("optimal value", problem.value)

print(x.value)
print(y.value)
