import numpy as np


def rmsprop(X, y, lr=0.01, gamma=0.9, epsilon=1e-8, epochs=100):
    """
    Performs RMSProp optimization for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        gamma: Decay rate for the moving average (typically around 0.9)
        epsilon: Small constant for numerical stability (float)
        epochs: Number of training epochs (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch (optional)
    """

    row, col = X.shape

    weights = np.zeros(col + 1)
    cache = np.zeros(col + 1)

    x_b = np.c_[np.ones((row, 1)), X]

    losses = []

    for _ in range(epochs):

        predictions = x_b @ weights

        errors = predictions - y

        gradients = 2 / len(X) * (x_b.T @ errors)

        cache = gamma * cache + (1 - gamma) * gradients**2

        weights -= (lr / np.sqrt(cache) + epsilon) * gradients

        loss = np.mean((errors) ** 2)
        losses.append(loss)

    return weights, losses
