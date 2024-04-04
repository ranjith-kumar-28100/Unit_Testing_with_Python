def sum_of_list(li):
    """Returns sum of all the numbers in a list
    >>> sum_of_list([0,9,8,0])
    17
    >>> sum_of_list([-1,5,6])
    10
    """

    total = 0
    for n in li:
        total += n

    return total


import doctest

if __name__ == "__main__":
    doctest.testmod()
