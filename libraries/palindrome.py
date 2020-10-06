def is_palindrome(N:int):
    """ Check if N is a palindrome

    Args:
        N (int): number

    Returns:
        bool: True if N is a palindrome else False
    """
    nstr = str(N)
    return nstr == nstr[::-1]