import scipy.stats as stats
import numpy as np


def ci_zscore(data, population_std, confidence_level=0.95):
    sample_size = len(data)
    sample_mean = sum(data) / sample_size
    z_score = stats.norm.ppf(0.5 + confidence_level / 2)
    lower_bound = sample_mean - z_score * population_std / np.sqrt(sample_size)
    upper_bound = sample_mean + z_score * population_std / np.sqrt(sample_size)

    print(
        f"Confidence Interval ({confidence_level*100:.0f}%): [{lower_bound:.4f}, {upper_bound:.4f}]"
    )


def ci_tscore(data, confidence_level=0.95):
    sample_size = len(data)
    sample_mean = sum(data) / sample_size
    sample_std = np.std(data)
    df = sample_size - 1
    t_score = stats.t.ppf(0.5 + confidence_level / 2, df)
    lower_bound = sample_mean - t_score * sample_std / np.sqrt(sample_size)
    upper_bound = sample_mean + t_score * sample_std / np.sqrt(sample_size)

    print(
        f"Confidence Interval ({confidence_level*100:.0f}%): [{lower_bound:.4f}, {upper_bound:.4f}]"
    )


# Example
# Imagine you're a bakery owner, and you want to estimate the average daily bread sales (population mean)
# based on a sample of sales data from the past week (sample).
# You'd also like to know the range of values that likely contains the true average with a 95% confidence level.

data = [25, 23, 28, 21, 24, 27, 22]

ci_tscore(data)
# Confidence Interval (95%): [22.0908, 26.4807]
