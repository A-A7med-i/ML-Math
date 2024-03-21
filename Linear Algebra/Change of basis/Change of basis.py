import sympy as sp

M = sp.Matrix([[2, 1, 3], [1, -1, 4]])

print(M.rref())
# (Matrix([
# [1, 0, 7 / 3],
# [0, 1, -5 / 3]]), (0, 1))
#  a = 7 / 3 , b = -5 / 3
