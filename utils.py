"""Utils"""


def reduce(function, iterable):
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = function(value, element)
    return value
