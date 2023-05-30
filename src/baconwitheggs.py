"""
1 - Receive an integer;
2 - Check if the number is a multiple of 3 and 5;
    R: Bacon with Eggs
3 - Check if the number is only multiple of 3;
    R: Bacon
4 - Check if the number is only multiple of 5;
    R: Eggs
5 - Check if the number is not multiple of either 3 or 5;
    R: Starving
"""


def bacon_with_eggs(n):
    assert isinstance(n, int), 'n must be an integer.'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon with Eggs'

    elif n % 3 == 0:
        return 'Bacon'

    elif n % 5 == 0:
        return 'Eggs'

    return 'Starving'
