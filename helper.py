#!/usr/bin/env python

def get_factors(num):
    factors = []
    for i in range(2, int(num/2) + 1):
        if not num%i:
            factors.append(i)
    return factors

def breadth_first(calc, filter, depth=4):
    nodes = [calc.root]
    for _ in range(depth):
        next_level = []
        for node in nodes:
            values = filter(node.value*10)
            for val in values:
                calc.add_nodes_binary(node, val)
            for n in node.binary_children:
                next_level.append(n[0])
                next_level.append(n[1])
        nodes = list(next_level)

def factorial_inverse(num):
    if num < 0:
        return 0
    num2 = num
    for i in range(1, num):
        if num2 % i:
            return 0
        else:
            num2 /= i
        if num2 == 1:
            return i
