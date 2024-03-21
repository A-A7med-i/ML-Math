import numpy as np


def diagonalization(matrix, pow):
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        D = np.diag(eigenvalues)
        P = eigenvectors

        if np.linalg.matrix_rank(P) == matrix.shape[0]:
            P_INV = np.linalg.inv(P)
            return P @ D**pow @ P_INV
        else:
            print("The matrix is not diagonalizable.")
    except Exception as e:
        print(f"Error: {e}")


M = np.array([[1, -3, 3], [3, -5, 3], [3, -3, 1]])

dig = diagonalization(M, 5)

print(dig)
