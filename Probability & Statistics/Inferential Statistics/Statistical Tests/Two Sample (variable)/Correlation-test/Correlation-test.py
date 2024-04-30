from scipy.stats import pearsonr
import numpy as np


ALPHA = 0.05


def correlation_test(*data):
    correlation_score, p_value = pearsonr(*data)

    print(f"Correlation score : {correlation_score:.4f} \nP value  : {p_value:.4f}")

    if p_value < ALPHA:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


weight = np.array(
    [
        3.63,
        3.02,
        3.82,
        3.42,
        3.59,
        2.87,
        3.03,
        3.46,
        3.36,
        3.3,
    ]
)

length = np.array([53.1, 49.7, 48.4, 54.2, 54.9, 43.7, 47.2, 45.2, 54.4, 50.4])


correlation_test(weight, length)

# output
# Correlation score : 0.4702
# P value  : 0.1703
# Fail to reject the null hypothesis
