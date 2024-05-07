import numpy as np


def momentum_gradient_descent(X, y, lr=0.01, gamma=0.9, epochs=100):
    """
    Performs momentum-based gradient descent for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        gamma: Momentum coefficient (typically between 0.8 and 0.99)
        epochs: Number of training epochs (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch
    """

    row, col = X.shape

    weights = np.zeros(col + 1)
    velocity = np.zeros(col + 1)

    x_b = np.c_[np.ones((row, 1)), X]

    losses = []

    for _ in range(epochs):

        prediction = x_b @ weights

        errors = prediction - y

        losses.append(np.mean(errors**2))

        gradients = 2 / row * (x_b.T @ errors)

        velocity = lr * gradients + gamma * velocity

        weights -= velocity

    return weights, losses
