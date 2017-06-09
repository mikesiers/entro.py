"""entro.py : Information Entropy Calculations

This module can be used to calculate various information entropy based
measurements. It is mainly intended for use in machine learning algorithms.

"""
import math

def calculate_entropy(support_true, support_false):
    """This function can be used to calculate information entropy.

    Args:
        support_true (int): The number of data points considered positive.
        support_false (int): The number of data points considered negative.

    Returns:
        (num): The information entropy given the two support counts.

    Raises:
        ValueError: If one or more of the support values are negative.

    """
    if (support_true < 0 or support_false < 0):
        raise ValueError('One or more input support values was negative.')
    support_total = support_true + support_false
    prior_true = support_true/support_total
    prior_false = support_false/support_total

    return  -prior_true * math.log(prior_true, 2) + \
            -prior_false * math.log(prior_false, 2)
