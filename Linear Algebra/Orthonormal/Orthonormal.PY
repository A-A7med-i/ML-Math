import numpy as np


def gram_schmidt(vectors):

    orthonormal_basis = []

    for v in vectors:
        projection = sum(
            np.dot(v.T, u) / np.linalg.norm(u) ** 2 * u for u in orthonormal_basis
        )
        u = v - projection
        if np.linalg.norm(u) > 1e-10:
            orthonormal_basis.append(u / np.linalg.norm(u))

    return np.around(orthonormal_basis[0], 3)


v1 = np.array([[1], [1], [0]])
v2 = np.array([[3], [2], [0]])

vectors = [v1, v2]

print(gram_schmidt(vectors))
