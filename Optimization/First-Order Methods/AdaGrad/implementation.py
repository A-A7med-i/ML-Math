import numpy as np


def adagrad(X, y, lr=0.01, eps=1e-8, epochs=100):
    """
    Performs AdaGrad for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        eps: Epsilon value for numerical stability (optional)
        epochs: Number of training epochs (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch (optional)
    """
    row, col = X.shape

    weights = np.zeros(col + 1)
    h = np.zeros(col + 1)

    losses = []

    x_b = np.c_[np.ones((row, 1)), X]

    for _ in range(epochs):
        prediction = x_b @ weights
        errors = prediction - y

        gradient = x_b.T @ errors

        h += gradient**2

        weights -= (lr / np.sqrt(h) + eps) * gradient

        losses.append(np.mean(errors**2))

    return weights, losses
