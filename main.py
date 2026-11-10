from math import sqrt


def norm(x, y):
    res = sqrt(x**2 + y**2)
    print(f"l1 norm: {res}")
    return res
