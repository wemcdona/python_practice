def list_check(lst):
    if (type(lst) is list):
        return True
    else:
        return False
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
