#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_total = 0
    scores_total = 0

    for score, weight in my_list:
        scores_total += score * weight
        weight_total += weight

    return scores_total / weight_total
