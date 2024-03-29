#!/usr/bin/env python
import math


def elementary(summand=0, factor=1, power=1):
    def inverse(result):
        ret = []
        temp = (result - summand) / factor
        if temp < 0 and 1 / power < 1:
            return []
        ret.append(temp ** (1 / power))
        if not power % 2:
            ret.append(- temp ** (1 / power))
        return ret
    return inverse


def factorial():
    def inverse(result):
        fact = 0
        arg = 1
        while fact < result:
            fact = math.factorial(arg)
            if fact == result:
                return [arg]
            arg += 1
        return []
    return inverse


def multiply_digits():
    def inverse(arg):

        return result
    return inverse


def multiply_digits():
    def inverse(arg):
        prime_factors = get_prime_factors(arg)
        if len(list(filter(lambda x: x>=10, prime_factors))):
            return []
        result = [int("".join(map(str, prime_factors)))]
        return result
    return inverse
