import numpy as np


v = np.array([[1], [2]])

print(v.shape)
# (2, 1)


# scaling the vector
S_M = np.array([[2, 0], [0, 2]])

print(S_M @ v)
# [[2][4]]

# Rotation the basis with 180 deg
R_M = np.array([[-1, 0], [0, -1]])

print(R_M @ v)
# [[-1][-2]]

# Shear in x - axis
SH_M = np.array([[1, 0.5], [0, 1]])

print(SH_M @ v)
# [[2.0][2.0]]


# Reflection
RE_M = np.array([[1, 0], [0, -1]])

print(RE_M @ v)
# [[1][-2]]
