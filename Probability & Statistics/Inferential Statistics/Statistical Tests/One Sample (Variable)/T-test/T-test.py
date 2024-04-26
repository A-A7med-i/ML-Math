from scipy.stats import ttest_1samp
import random


def t_test(data, mean, alternative="two-sided"):
    t_score, p_value = ttest_1samp(data, popmean=mean, alternative=alternative)

    print(f"T-Statistic: {t_score:.4f}")
    print(f"p-value: {p_value:.4f}")
    if p_value < 0.05:
        print(
            "Reject null hypothesis (H₀). Sample mean is statistically different from 100."
        )
    else:
        print(
            "Fail to reject null hypothesis (H₀). Not enough evidence to conclude a difference from 100."
        )


# Example:
# Suppose a botanist wants to know if the mean height of a certain species of plant
# is equal to 15 inches. She collects a random sample of 12 plants and records each of their heights in inches.

plant_heights = []
for _ in range(12):
    plant_heights.append(random.uniform(15 - 2, 15 + 2))

t_test(plant_heights, 15)
