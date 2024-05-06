import numpy as np


def stochastic_gradient_descent(X, y, lr=0.001, epochs=100, size_batch=1):
    row, col = X.shape

    weights = np.zeros(col + 1)

    losses = []

    X_b = np.c_[np.ones((row, 1)), X]

    for epoc in range(epochs):
        for i in range(0, row, size_batch):

            batch_X = X_b[i : i + size_batch]
            batch_y = y[i : i + size_batch]

            predictions = batch_X @ weights
            errors = predictions - batch_y

            loss = np.mean(errors**2)
            losses.append(loss)

            gradients = (errors.reshape(-1, 1) * batch_X).mean(axis=0)
            weights -= lr * gradients

    return weights, losses
