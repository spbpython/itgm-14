import itertools


def foo():
    a, b = 0, 1

    while True:
        yield a
        ...


print([*itertools.islice(foo(), 10)])
