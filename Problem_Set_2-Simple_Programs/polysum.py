from math import tan, pi

def polysum(n, s):
    return round((0.25 * n * s ** 2) / tan(pi / n) + (n * s) ** 2, 4)

print polysum(43, 1)