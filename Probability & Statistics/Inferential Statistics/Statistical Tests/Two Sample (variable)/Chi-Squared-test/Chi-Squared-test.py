import numpy as np
import seaborn as sns
from scipy.stats import chisquare
from scipy.stats import chi2_contingency


ALPHA = 0.05

chi = np.zeros(1000)


for _ in range(50):
    d1 = np.random.normal(size=1000)
    chi += d1**2

sns.histplot(chi, kde=True)


def chi_squared_test(op):
    chi_score, p_value = chisquare(op)

    print(f"chi score : {chi_score:.4f} \nP value  : {p_value:.4f}")

    if p_value < ALPHA:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


def chi_squared_test_two(data):
    chi_score, p_value, df, expected_values = chi2_contingency(data)

    print(
        f"chi score : {chi_score:.4f} \nP value  : {p_value:.4f}\ndegree of freedom {df}\nexpected_values : \n{np.round(expected_values,4)})"
    )

    if p_value < ALPHA:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


# Example
# Youʼre hired by a dog food company to help them test three new dog food
# flavors.
# You recruit a random sample of 75 dogs and offer each dog a choice between
# the three flavors by placing bowls in front of them. You expect that the flavors
# will be equally popular among the dogs, with about 25 dogs choosing each
# flavor.
# Null hypothesis : p1 = p2 = p3
# Alternative hypothesis (Ha): p1 != p2 != p3


op = np.array([22, 30, 23])


chi_squared_test(op)


# Example
# Imagine a city wants to encourage more of its residents to recycle their
# household waste.
# The city decides to test two interventions: an educational flyer(pamphlet) or a
# phone call. They randomly select 300 households and randomly assign them to
# the flyer, phone call, or control group (no intervention). Theyʼll use the results
# of their experiment to decide which intervention to use for the whole city.
# The city plans to use a chi-square test of independence to test whether the
# proportion of households who recycle differs between the interventions.


data = [[89, 9], [84, 8], [86, 24]]

chi_squared_test_two(data)
