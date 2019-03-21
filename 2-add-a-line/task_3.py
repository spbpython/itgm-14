import typing


def devs(n: int) -> typing.MutableSequence[int]:
    result = []

    for x in range(1, n + 1):
        ...
            result.append(x)

    return result


print(devs(12))
