#!/usr/bin/env python


def multiplication(factor=1, summand=0):
    def inverse(total, arg):
        return [((total - summand) / factor) / arg]
    return inverse


def division(operator1=lambda x:x, inverse1=lambda x:[x], operator2=lambda x:x, inverse2=lambda x:[x]):
    def inverse(total, arg):
        ret = inverse2(total * operator1(arg))
        ret.extend(inverse1(operator2(arg) / total))
        return list(set(ret))
    return inverse


def sum(operator1, inverse1, operator2, inverse2):
    def inverse(total, arg):
        ret = inverse2(total - operator1(arg))
        ret.extend(inverse1(total - operator2(arg)))
        return list(set(ret))
    return inverse
