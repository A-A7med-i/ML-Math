import numpy as np


def nesterov_accelerated_gradient_descent(X, y, lr=0.01, gamma=0.9, epochs=100):
    """
    Performs Nesterov Accelerated Gradient Descent for linear regression.

    Args:
        X: Feature matrix (shape: n_samples, n_features)
        y: Target values (shape: n_samples)
        lr: Learning rate (float)
        gamma: Momentum coefficient (typically between 0.8 and 0.99)
        epochs: Number of training epochs (int)

    Returns:
        weights: Learned weights (shape: n_features + 1)
        losses: List of loss values per epoch (optional)
    """

    row, col = X.shape

    weights = np.zeros(col + 1)
    velocity = np.zeros(col + 1)

    x_b = np.c_[np.ones((row, 1)), X]

    losses = []

    for _ in range(epochs):

        weights_temp = weights - gamma * velocity

        predictions_temp = x_b @ weights_temp

        errors = predictions_temp - y

        gradients = 2 * x_b.T.dot(errors) / row

        velocity = gamma * velocity + lr * gradients
        weights -= velocity

        predictions = x_b.dot(weights)
        loss = np.mean((predictions - y) ** 2)
        losses.append(loss)

    return weights, losses
