def verify_int_or_float(lst: list[int | float]) -> bool:
    """Check if all elements in a list are integers or floats

    Args:
        lst (list[int | float]): A list of integers or floats

    Returns:
        bool: True if all elements are integers or floats, False otherwise

    """

    if not all(isinstance(h, (int, float))
               and not isinstance(h, bool) for h in lst):

        return False

    return True


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:

    """Calculate the BMI of a list of people

    Args:
        height (list[int | float]): A list of heights
        weight (list[int | float]): A list of weights

    Returns:
        list[int | float]: A list of BMIs
    """

    if len(height) != len(weight):
        return []

    if not verify_int_or_float(height) or not verify_int_or_float(weight):
        return []

    return [w / (h * h) for w, h, in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int | float) \
        -> list[bool]:

    """Apply a limit to the BMI of a list of people

    Args:
        bmi (list[int | float]): A list of BMIs
        limit (int | float): The limit to apply

    Returns:
        list[bool]: Return a list of booleans, true if the bmi is above the \
            limit and false otherwise
    """

    return [b > limit for b in bmi]
