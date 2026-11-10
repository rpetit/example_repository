from math import sqrt


def norm(x, y, ord=2):
    if ord == 2:
        return sqrt(x**2 + y**2)
    elif ord == 1:
        return abs(x) + abs(y)
    else:
        raise ValueError("The only values allowed for ord are 1 and 2")
