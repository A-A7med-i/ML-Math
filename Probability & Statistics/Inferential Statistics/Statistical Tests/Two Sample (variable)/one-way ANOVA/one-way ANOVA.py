from scipy.stats import f_oneway

ALPHA = 0.05


def one_way_anova(*groups):
    f_score, p_value = f_oneway(*groups)

    print(f"f score : {f_score:.4f} \nP value  : {p_value:.4f}")

    if p_value < ALPHA:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


# Example

group1 = [89, 92, 87, 90]
group2 = [78, 82, 75, 80]
group3 = [95, 98, 97, 99]

one_way_anova(group1, group2, group3)

# output
# f score : 64.0670
# P value  : 0.0000
# Reject the null hypothesis
