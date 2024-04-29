from scipy.stats import ttest_ind

alpha = 0.05


def independent_t_test(data_1, data_2):
    t_score, p_value = ttest_ind(data_1, data_2)
    print(f"t score : {t_score:.4f} \nP value  : {p_value:.4f}")

    if p_value < alpha:
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


call_center1 = [12.5, 11.2, 13.1, 10.8, 11.9, 10.5, 12.4, 12.9, 11.7, 13.2]

call_center2 = [14.3, 13.1, 15.2, 12.7, 13.9, 13.5, 14.1, 12.8, 13.7, 15.5]

independent_t_test(call_center1, call_center2)
