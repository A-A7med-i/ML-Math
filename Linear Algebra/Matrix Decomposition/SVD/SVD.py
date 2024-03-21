import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

U, Sigma, Vt = np.linalg.svd(A)

left_singular_vectors = np.around(U, 3)
singular_values = np.around(np.diag(Sigma), 3)
right_singular_vectors = np.around(Vt.T, 3)

print("Left singular vectors:\n", left_singular_vectors)
print("Singular values:\n", singular_values)
print("Right singular vectors:\n", right_singular_vectors)

# Left singular vectors:
#  [[-0.215  0.887  0.408]
#  [-0.521  0.25  -0.816]
#  [-0.826 -0.388  0.408]]
# Singular values:
#  [[16.848  0.     0.   ]
#  [ 0.     1.068  0.   ]
#  [ 0.     0.     0.   ]]
# Right singular vectors:
#  [[-0.48  -0.777 -0.408]
#  [-0.572 -0.076  0.816]
#  [-0.665  0.625 -0.408]]
