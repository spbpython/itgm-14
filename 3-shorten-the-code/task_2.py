import typing


def queue_time(customers: typing.MutableSequence[float], n: int) -> float:

    if not customers:
        return 0.0

    tills = customers[:n]
    customers = customers[n:]
    customers.reverse()

    while customers:
        tills.sort()
        tills[0] += customers.pop()

    return max(tills)


print(queue_time(customers=[3.5, 1.2, 5.0, 4.5, 1.0], n=3))
# >>> 5.7
