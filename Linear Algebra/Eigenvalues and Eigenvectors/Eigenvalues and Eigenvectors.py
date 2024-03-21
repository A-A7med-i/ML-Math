import numpy as np

v1 = np.array([[1, 2], [5, 4]])

eig_val, eig_vec = np.linalg.eig(v1)

print(eig_val)

print(np.around(eig_vec))

v2 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])

eig_val, eig_vec = np.linalg.eig(v2)

print(np.round(eig_val))

print(np.around(eig_vec))
