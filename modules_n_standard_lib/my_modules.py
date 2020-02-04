# this module will be used by other modules
print('This is an imported module')
test_string = 'Test String'


def find_index(to_search, target):
    """Finds the index of a value in the sequence

    Args:
        to_search (list): list to search from
        target (string): what we are looking for
    """
    for i, value in enumerate(to_search):
        if value == target:
            return i
        else:
            return -1
