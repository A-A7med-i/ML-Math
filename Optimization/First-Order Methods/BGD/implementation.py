import numpy as np


def batch_gradient_descent(X, y, lr=0.001, epochs=100):

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
