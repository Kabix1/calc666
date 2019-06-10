#!/usr/bin/env python

import helper
import calc666
import math

def stage19_inverse(d, q):
    return [-d/q]

def stage19():
    calculator = calc666.Calc666([".", "1", "2"], binary_inverse=stage19_inverse)
    factors = helper.get_factors(666)
    nodes = [calculator.root]
    for i in range (1, 3):
        next_level = []
        for node in nodes:
            print(node)
            factors = helper.get_factors(node.value)
            for val in factors:
                calculator.add_nodes_binary(node, val)
            for n in node.binary_children:
                next_level.append(n[0])
                next_level.append(n[1])
        nodes = list(next_level)


def stage20_inverse(total, arg):
    res1 = (total / 2)
    res2 = (total - arg * 2) / 20
    return [res1, res2]


def stage20():
    calculator = calc666.Calc666([], binary_inverse=stage20_inverse)
    for i in range(600):
        calculator.add_nodes_binary(calculator.root, i)

def stage21_inverse(total, arg):
    return [(total - arg/2)*2]

def stage21():
    calculator = calc666.Calc666(["6"], binary_inverse=stage21_inverse)
    for i in range(600):
        calculator.add_nodes_binary(calculator.root, i)

def stage22_inverse(d, q):
    return [d/q]

def stage22():
    calculator = calc666.Calc666([".", "1", "2", "5", "9"], binary_inverse=stage22_inverse)
    helper.breadth_first(calculator, helper.get_factors)


def stage23_inverse(total, arg):
    return [(total-arg**2)**0.5]


def stage23():
    calculator = calc666.Calc666(["."], binary_inverse=stage23_inverse)
    for i in range(666):
        calculator.add_nodes_binary(calculator.root, i)

def stage24_inverse(total, arg):
    ret1 = (total / arg)-1
    ret2 = total / (arg - 1)
    return [ret1, ret2]

def stage24():
    calc = calc666.Calc666(["2", "6"],
                           binary_inverse=stage24_inverse)
    helper.breadth_first(calc, helper.get_factors)

def stage25_inverse(total, arg):
    ret1 = (total + arg**2) / arg
    return [ret1]

def stage25():
    calc = calc666.Calc666(["5", "7"],
                           binary_inverse=stage25_inverse)
    helper.breadth_first(calc, helper.get_factors)


def stage27_inverse(total, arg):
    results = []
    sum = 0
    i = arg
    while sum < total:
        sum += i
        i += 1
    if sum == total:
        results.append(i-1)
    sum = 0
    i = arg
    while 0 < sum < total:
        sum += i
        i -= 1
    if sum == total:
        results.append(i+1)
    return results

def stage27():
    calc = calc666.Calc666(["6"], binary_inverse=stage27_inverse)
    for i in range(666):
        calc.add_nodes_binary(calc.root, i)

def stage30_inverse(total, arg):
    result_cubed = (total - 1 - arg**3)
    if result_cubed > 0:
        result = result_cubed**(1/3)
    else:
        result = - ((- result_cubed) ** (1/3))
    return [result]

def stage30():
    calc = calc666.Calc666(["."], binary_inverse=stage30_inverse)
    helper.breadth_first(calc, range, 3)

def stage40_inverse(total, arg):
    result1 = total**2 - arg*11
    result2 = (total**2 - arg) / 11
    return [result1, result2]

def stage40():
    calc = calc666.Calc666(["6"], binary_inverse=stage40_inverse)
    for i in range(666**2):
        calc.add_nodes_binary(calc.root, i)

def stage41_inverse(total, arg):
    result1 = total / 10 * arg
    result2 = 10 / arg / total
    return [result1, result2]

def stage41():
    calc = calc666.Calc666(["4", "2", "6", "."], binary_inverse=stage41_inverse)
    for i in range(1, 666):
        calc.add_nodes_binary(calc.root, i)

def stage42_inverse(total, arg):
    if arg:
        return [total/arg]
    else:
        return []

def stage42():
    calc = calc666.Calc666(["4", "5", "6", "9", "2"], binary_inverse=stage42_inverse)
    helper.breadth_first(calc, range, 3)

def stage43():
    calc = calc666.Calc666(["1", "2", "4", "5", "6", "7"], binary_inverse=stage42_inverse)
    calc.root.value = 6*7*7+6*7+6
    helper.breadth_first(calc, range, 3)


def stage45_inverse(total, arg):
    if arg > 0:
        results = []
        result1 = helper.factorial_inverse(total - math.factorial(arg))
        result2 = helper.factorial_inverse(total + math.factorial(arg))
        if result1:
            results.append(result1)
        if result2:
            results.append(result2)
        return results
    else:
        return []

def stage45():
    calc = calc666.Calc666([], binary_inverse=stage45_inverse)
    for i in range(1, 15):
        calc.add_nodes_binary(calc.root, i)

def stage47():
    calc = calc666.Calc666(["8", "9", "6"], binary_inverse=stage40_inverse)
    for i in range(666**2):
        calc.add_nodes_binary(calc.root, i)

if __name__ == "__main__":
    stage47()
