from statsmodels.stats.weightstats import ztest
import random


def z_test_two_sample(start, stop, size, alternative="two-sided"):
    data_1 = [random.randint(start, stop) for _ in range(size)]
    data_2 = [random.randint(start, stop) for _ in range(size)]

    z_score, p_value = ztest(data_1, data_2, value=0, alternative=alternative)
    print(f"z score : {z_score:.4f} \nP value  : {p_value:.4f}")


# Suppose the IQ levels among individuals in two different cities are known to be normally distributed with known standard deviations.

# A researcher wants to know if the mean IQ level between individuals in city A and city B are different,
# so she selects a simple random sample of  20 individuals from each city and records their IQ levels.

# H0 : MEAN1 = MEAN2
# H1 : MEAN1 != MEAN2

z_test_two_sample(90, 150, 20)
