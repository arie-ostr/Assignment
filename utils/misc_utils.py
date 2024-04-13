
def n_lists_of_lists_are_same(list_of_lists):
    """
        makes sure there is no equal pair among n-items
    """
    seen = set()
    for lst in list_of_lists:
        tuple_version = tuple(lst)  # Convert list to tuple
        if tuple_version in seen:
            return False  # Found a duplicate list
        seen.add(tuple_version)
    return True