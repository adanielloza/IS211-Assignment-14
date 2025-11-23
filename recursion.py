def fibonnaci(n):
    """
    Return the n-th Fibonacci number using recursion.

    Parameters:
        n (int): non-negative index of the Fibonacci sequence

    Returns:
        int: n-th Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    """
    Return the greatest common divisor (GCD) of two integers
    using Euclid's recursive algorithm.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    """
    Recursively compare two strings lexicographically.

    Returns:
        negative int: if s1 < s2
        0:            if s1 == s2
        positive int: if s1 > s2
    """
    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return -1
    if s2 == "":
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])