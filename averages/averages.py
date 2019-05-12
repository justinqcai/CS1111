#Justin Cai, jc5pz
import math


def mean(a, b, c):
    return (a+b+c)/3


def median(a, b, c):
    if a > b:
        if c > a:
            return a
        if c > b:
            return c
        return b
    else:
        if c > b:
            return b
        if c > a:
            return c
        return a


def rms(a, b, c):
    return math.sqrt(mean(a**2, b**2, c**2))


def middle_average(a, b, c):
    m = mean(a, b, c)
    med = median(a, b, c)
    r = rms(a, b, c)
    return median(m, med, r)

