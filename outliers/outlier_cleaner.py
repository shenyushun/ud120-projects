#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    # your code goes here
    for i, v in enumerate(ages):
        cleaned_data.append(
            (v, net_worths[i], abs(
                net_worths[i] - predictions[i])))
    cleaned_data = sorted(cleaned_data,
                          key=lambda x: x[-1],
                          reverse=True)[int(len(cleaned_data) * 0.1):]
    print(len(cleaned_data))
    return cleaned_data
