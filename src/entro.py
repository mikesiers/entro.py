"""entro.py : Information Entropy Calculations

This module can be used to calculate various information entropy based
measurements. It is mainly intended for use in machine learning algorithms.

"""
import math

def calculate_entropy(supports):
    """This function can be used to calculate information entropy.

    Args:
        supports (array<int>): The number of data points for each class value.

    Returns:
        (num): The information entropy given the support counts.

    Raises:
        ValueError: If one or more of the support values are 0 or less.

    """
    if any(i <= 0 for i in supports):
        raise ValueError('One or more input support values was 0 or less.')
    support_total = sum(supports)

    entropy = 0
    priors = [x / support_total for x in supports]
    for prior in priors:
        entropy += -prior * math.log(prior, 2)

    return entropy
