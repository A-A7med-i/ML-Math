import numpy as np


def mini_batch_gradient_descent(X, y, lr=0.001, epochs=100, batch_size=32):
    """
    Performs mini-batch gradient descent for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        epochs: Number of training epochs (int)
        batch_size: Mini-batch size (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch
    """

    row, col = X.shape
    weights = np.zeros(col + 1)

    losses = []

    x_b = np.c_[np.ones((row, 1)), X]

    for _ in range(epochs):
        for i in range(0, row, batch_size):
            x_batch = x_b[i : i + batch_size]
            y_batch = y[i : i + batch_size]

            predictions = x_batch @ weights
            errrors = predictions - y_batch

            gradients = 2 / batch_size * (x_batch.T @ errrors)
            weights -= lr * gradients

        losses.append(np.mean(errrors**2))

    return weights, losses
