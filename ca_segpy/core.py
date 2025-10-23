def C(a, b):
    """
    Compare pixel 'a' to its neighborhood 'b' and determine the majority direction.
    Returns:
        1  if most neighbors > a
        -1 if most neighbors < a
         0 if balanced
    """
    higher = sum(val > a for val in b)
    lower = sum(val < a for val in b)
    if higher > lower:
        return 1
    elif lower > higher:
        return -1
    return 0


def majority_function(central_pixel, neighborhood):
    """
    Updates the central pixel according to the majority function.
    """
    majority = C(a=central_pixel, b=neighborhood)
    if majority == 1:
        central_pixel += 1
    elif majority == -1:
        central_pixel -= 1
    return central_pixel
