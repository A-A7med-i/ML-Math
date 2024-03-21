import numpy as np
import sympy as sp

m1 = np.array([[2, 1, 1], [4, 2, 6]])

m1 = sp.Matrix(m1)

print(m1)


# (Matrix([
#  [1, 1/2, 0],
#  [0,   0, 1]]),
#  (0, 2))
print(m1.rref())  # no solution


m2 = np.array([[6, 4, 3, -6], [1, 2, 1, 1 / 3], [-12, -10, -7, 11]])

m2 = sp.Matrix(m2)

print(m2)


# (Matrix([
# [1, 0, 0, -0.666666666666667],
# [0, 1, 0, 2.5],
# [0, 0, 1, -4.0]]),
# (0, 1, 2))


print(m2.rref())

# the solution is x = -0.667 , y = 2.5, z = -4.0
