def f(seq_a, seq_b):
    """checks if sequence a is a subset of b

    Args:
        seq_a (iterable): Description
        seq_b (iterable): Description

    Returns:
        Boolean: Description
    """
    is_subset = True
    for x in seq_a:
        if x not in seq_b:
            is_subset = False
    return is_subset


print(f([1, 3, 8], [1, 3, 4, 5]))
