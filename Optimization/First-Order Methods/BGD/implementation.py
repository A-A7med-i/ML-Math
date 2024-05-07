import numpy as np


def batch_gradient_descent(X, y, lr=0.001, epochs=100):
    """
    Performs batch gradient descent (BGD) for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        epochs: Number of training epochs (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch
    """

    row, col = X.shape

    weights = np.zeros(col + 1)

    losses = []

    X_b = np.c_[np.ones((row, 1)), X]

    for _ in range(epochs):

        predictions = X_b.dot(weights)

        errors = predictions - y

        loss = np.mean(errors**2)

        losses.append(loss)

        gradient = 2 / row * (X_b.T.dot(errors))

        weights -= gradient * lr

    return weights, losses
