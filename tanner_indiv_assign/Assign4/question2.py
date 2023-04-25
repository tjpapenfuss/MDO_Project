from scipy import linalg
import numpy as np


A = np.array([[1, 4, 5, 6], [0.2, 0.7, 0.9, 0.1],
              [4, 6, 1, 0], [7, 8, 8, 7],
              [2.4, 1.7, 2.9, -1.1], [12, 8, 7, 1]])
A_transpose = np.transpose(A)
ns = linalg.null_space(A_transpose)

print(ns)

