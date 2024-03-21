import numpy as np
from math import inf

v = np.array([[3], [-4]])

# (2, 1)
print(v.shape)

# default is norm 2
l2 = np.linalg.norm(v)
l1 = np.linalg.norm(v, 1)
l_inf = np.linalg.norm(v, inf)

# 7.0 5.0 4.0

print(l1, l2, l_inf)


v1 = np.array([[3], [-4]])
v2 = np.array([[1], [2]])

# [-5]
print(*(v1.T @ v2))


# [[ 4]
#  [-2]]
print(v1 + v2)
