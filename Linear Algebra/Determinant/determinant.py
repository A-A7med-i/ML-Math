import numpy as np


def determinant(matrix):
    det = np.linalg.det(matrix)
    return det.round()


m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[3, 4], [1, 2]])
m3 = np.array([[4, 2], [2, 1]])
m4 = np.array([[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]])


# -2.0
print(determinant(m1))


# 2.0
print(determinant(m2))

# 0.0
print(determinant(m3))

# 30.0
print(determinant(m4))
