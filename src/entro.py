"""entro.py : Information Entropy Calculations

This module can be used to calculate various information entropy based
measurements. It is mainly intended for use in machine learning algorithms.

"""
import math

def entropy(supports):
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

def info_gain(splits, parent_supports):
    """This function can be used to calculate information gain.

    Args:
        splits (array<array<int>>): A multi dimensional array containing
                                    the number of data points for each
                                    class value such that splits[i][j]
                                    contains the number of data points
                                    belonging to the i'th split and j'th
                                    class value.

    Returns:
        (num): The information gain given the support counts of the splits.

    Raises:
        ValueError: If one or more of the support values are 0 or less.
    
    """
    weighted_entropies = []
    for split in splits:
        if any(i <= 0 for i in split):
            raise ValueError('One or more input support values was 0 or less.')
        split_entropy = (entropy(split))
        weight = sum(split)/sum(parent_supports)
        weighted_entropies.append(weight * split_entropy)

    return entropy(parent_supports) - sum(weighted_entropies)

def split_info(split_sizes, parent_size):
    """This function can be used to calculate split information.

    Args:
        split_sizes (array<int>): The number of data points in each split.

    Returns:
        (num): The split information calculated from the given split sizes.

    Raises:
        ValueError: If one or more of the sizes are 0 or less.
    
    """
    if any(i <= 0 for i in split_sizes) or parent_size <= 0:
        raise ValueError('One or more input split sizes was 0 or less.')
    weighted_sizes = [x / parent_size for x in split_sizes]
    individual_split_infos = [x * math.log(x, 2) for x in weighted_sizes]
    return -1 * sum(individual_split_infos)
