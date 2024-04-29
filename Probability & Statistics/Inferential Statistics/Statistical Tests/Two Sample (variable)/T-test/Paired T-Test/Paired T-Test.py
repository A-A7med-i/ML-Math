from scipy.stats import ttest_rel


def paired_t_test(pre, post):
    t_score, p_value = ttest_rel(pre, post)
    print(f"t score : {t_score:.4f} \nP value  : {p_value:.4f}")


pre = [88, 82, 84, 93, 75, 78, 84, 87, 95, 91, 83, 89, 77, 68, 91]
post = [91, 84, 88, 90, 79, 80, 88, 90, 90, 96, 88, 89, 81, 74, 92]


# Example: Paired Samples T-Test in Python
# Suppose we want to know whether a certain study program significantly impacts student performance on a particular exam.
# To test this, we have 15 students in a class take a pre-test.
# Then, we have each of the students participate in the study program for two weeks.
# Then, the students retake a test of similar difficulty.

paired_t_test(pre, post)
