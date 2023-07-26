def multiple_letter_count(phrase):
    d = {}
    for i in phrase:
        d[i] = d.get(i,0)+1
    return d
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """