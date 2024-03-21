import numpy as np
import sympy as sp

M = np.array([[2, 1, -1], [1, 2, 4]])
M = sp.Matrix(M)

print(M.rref())
# (Matrix([
#  [1, 0, -2],
#  [0, 1, 3]]),
#  (0, 1))
# one sol
# a = -2 , b = 3
