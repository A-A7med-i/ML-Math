import numpy as np

m1 = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(m1))

# [[-2.   1. ]
#  [ 1.5 -0.5]]

m2 = np.array([[3, -1], [-9, 3]])


# LinAlgError: Singular matrix
# print(np.linalg.inv(m2))
