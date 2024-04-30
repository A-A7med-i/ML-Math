import numpy as np

data = np.array(
    [
        [10, 80],
        [13, 90],
        [15, 95],
        [11, 85],
    ]
)


x = data[:, 0]
y = data[:, 1]

covariance_matrix = np.round(np.cov(x, y), 4)

correlation = np.round(np.corrcoef(x, y), 4)

print("Covariance:", covariance_matrix)

print("Correlation:", correlation)
