from statsmodels.stats.weightstats import ztest
import random


def z_test(size, mean_sample, std_sample, mean_claim, alternative="two-sided"):
    data = [random.gauss(mean_sample, std_sample) for _ in range(size)]
    z_score, p_value = ztest(data, value=mean_claim, alternative=alternative)

    print(f"z-Statistic: {z_score:.4f}")
    print(f"p-value: {p_value:.4f}")
    if p_value < 0.05:
        print(
            "Reject null hypothesis (H₀). Sample mean is statistically different from 100."
        )
    else:
        print(
            "Fail to reject null hypothesis (H₀). Not enough evidence to conclude a difference from 100."
        )


# Example :
# Suppose the IQ in a certain population is normally
# distributed with a mean of μ = 100 and standard deviation of σ = 15.
# A researcher wants to know if a new drug affects IQ levels,
# so he recruits 20 patients to try it and records their IQ levels.
# determine if the new drug causes a significant difference in IQ levels:
# H0 : MEAN = 100
# H1 : MEAN != 100


z_test(20, 95, 100, 15)


# Example :
# A teacher claims that the mean score of students in his class is greater than 82
# with a standard deviation of 20. If a sample of 81 students was selected
# with a mean score of 90 then check if there is enough evidence to support this claim at a 0.05 significance level.
# H0 : MEAN = 82
# H1 : MEAN > 82


z_test(81, 90, 82, 20, "larger")
