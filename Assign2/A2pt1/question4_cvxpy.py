import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

x = cp.Variable()
y = cp.Variable()


objective_fn = (x**2 + y**2)
objective = cp.Minimize(objective_fn)
constraints = [y**2 - (x - 1)**3 == 0, x>=0, y>=0]
#constraints = [a*(x*y + x*z + y*z) <= b, x >= y**c]
problem = cp.Problem(objective, constraints)
#plt.plot(objective_fn)
print(np.pi)
print(problem.is_dgp(dpp=True))

problem.solve()
print("status:", problem.status)
print("optimal value", problem.value)

print(x.value)
print(y.value)
