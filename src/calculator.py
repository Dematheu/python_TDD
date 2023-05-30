def soma(x, y):
    """Soma x e y

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be int or float.
    """
    assert isinstance(x, (int, float)), 'x needs to be int or float.'
    assert isinstance(y, (int, float)), 'y needs to be int or float.'
    return x + y


def subtrai(x, y):
    """
    Subtrai x e y

    >>> subtrair(10, 5)
    5

    >>> subtrair('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be int or float.
    """
    assert isinstance(x, (int, float)), 'x needs to be int or float.'
    assert isinstance(y, (int, float)), 'y needs to be int or float.'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
