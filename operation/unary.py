#!/usr/bin/env python
import math


def elementary(summand=0, factor=1, power=1):
    def operator(arg):
        return summand + factor*(arg**power)
    return operator


def factorial():
    def operator(arg):
        return math.factorial(arg)
    return operator
