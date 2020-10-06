def sum_of_squares_of_N_natural_numbers(N:int):
    """ Sum of squares of first N natural numbers

    Args:
        N (int): number

    Returns:
        int: sum
    """
    return N*(N+1)*(2*N+1)//6

def sum_of_N_natural_numbers(N:int):
    """ Sum of first N natural numbers

    Args:
        N (int): number

    Returns:
        int: sum
    """
    return N*(N+1)//2