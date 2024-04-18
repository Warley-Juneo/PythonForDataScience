def slice_me(family: list, start: int, end: int) -> list:
    """ Given a 2D list, return a new 2D list that is a slice
    of the original list.
    The slice should be from the start index to the end index (exclusive).
    If the start index is greater than the end index, return an empty list.
    If the start index is greater than the length of the list,
    return an empty list.

    Args:
        family (list): A 2D list of strings.
        start (int): The index to start the slice.
        end (int): The index to end the slice.

    Returns:
        list: A 2D list of strings.
    """

    try:
        if start > len(family) or end > len(family):
            raise ValueError("Start or end index is greater than the \
                length of the list")

        if not isinstance(family, list):
            raise ValueError("Family must be a list")

        elif not all(isinstance(sublist, list) for sublist in family):
            raise ValueError("All elements of family must be lists")

        elif not all(len(family[0]) == len(sublist) for sublist in family):
            raise ValueError("All sublists must have the same length")
    except ValueError:
        return []

    print(f"My shape is : ({len(family)}, {len(family[0])})")
    new_family = family[start:end]
    print(f"My new shape is : ({len(new_family)}, {len(new_family[0])})")

    return new_family
