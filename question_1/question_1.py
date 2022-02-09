def sort_and_remove_duplicate(lst: list):
    """
    Sort a list before removing duplicates.
    List must contain only integer elements.
    """
    assert isinstance(lst, list), 'input must be list.'
    assert all([isinstance(v, int) and not isinstance(v, bool)
               for v in lst]), 'list elements must be integer.'

    lst.sort()
    new_list = []
    for v in lst:
        if v not in new_list:
            new_list.append(v)
    return new_list
