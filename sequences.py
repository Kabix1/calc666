#!/usr/bin/env python

def fibonacci(num):
    fib = [0, 1]
    for i in range(2, num):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def primes(num):
    integers = list(range(num**2))
    ret = []
    for i in integers:
        if i > 1:
            ret.append(i)
            for i2 in range(2*i, len(integers), i):
                integers[i2] = 0
    return ret[:num]


def josephus(num):
    a = [0, 1]
    for i in range(1, int(num/2) + 1):
        a.append(2 * a[i] - 1)
        a.append(2 * a[i] + 1)
    return a[:num]
