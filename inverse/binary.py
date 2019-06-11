#!/usr/bin/env python


def multiplication(operation1=lambda x:x, inverse1=lambda x:[x],
                   operation2=lambda x:x, inverse2=lambda x:[x],
                   summand=0):
    def inverse(total, arg):
        ret = inverse2((total - summand) / operation1(arg))
        ret.extend(inverse1((total - summand) / operation2(arg)))
        return list(set(ret))
    return inverse


def division(operation1=lambda x:x, inverse1=lambda x:[x],
             operation2=lambda x:x, inverse2=lambda x:[x]):
    def inverse(total, arg):
        ret = inverse2(total * operation1(arg))
        ret.extend(inverse1(operation2(arg) / total))
        return list(set(ret))
    return inverse


def sum(operation1=lambda x:x, inverse1=lambda x:[x],
             operation2=lambda x:x, inverse2=lambda x:[x]):
    def inverse(total, arg):
        ret = inverse2(total - operation1(arg))
        ret.extend(inverse1(total - operation2(arg)))
        return list(set(ret))
    return inverse
