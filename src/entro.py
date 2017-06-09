def calculate_entropy(support_true, support_false):
    if (support_true < 0 or support_false < 0):
        raise ValueError('One or more input support values was negative.')
    support_total = support_true + support_false
    prior_true = support_true/support_total
    prior_false = support_false/support_total

    return  prior_true * math.log(prior_true, 2) +
            prior_false * math.log(prior_false, 2)
