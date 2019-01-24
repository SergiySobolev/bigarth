import numpy as np


def add(a, b, r=10):
    carry = 0
    k = len(a)
    l = len(b)
    if k < l:
        a, b = b, a
        k, l = l, k
    c = np.zeros(k + 1)
    for i in range(l):
        tmp = a[i] + b[i] + carry
        (carry, c[i]) = quo_rem(tmp, r)
    for i in range(l,k-1):
        tmp = a[i] + carry
        (carry, c[i]) = quo_rem(tmp, r)
    if carry == 0:
        c = c[:-1]
    else:
        c[k] = carry
    return np.flipud(c)


def mul(a, b, r=10):
    k = len(a)
    l = len(b)
    if k < l:
        a, b = b, a
        k, l = l, k
    c = np.zeros(k + l)
    for i in range(k):
        carry = 0
        for j in range(l):
            tmp = a[i] * b[j] + c[i+j] + carry
            (carry, c[i + j]) = quo_rem(tmp, r)
        c[i + l] = carry
    if c[k + l - 1] == 0:
        c = c[:-1]
    return np.flipud(c)


def quo_rem(a, b):
    return a // b, a % b