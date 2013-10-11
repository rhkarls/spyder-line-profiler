#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
:author: Joseph Martinot-Lagarde

Created on Sat Jan 19 14:57:57 2013
"""

from __future__ import (
    print_function, division, unicode_literals, absolute_import)


import subdir.profiling_test_script2 as script2


@profile
def fact(n):
    result = 1
    for i in xrange(2, n + 1):
        result *= i
    return result


@profile
def sum_(n):
    result = 0

    for i in xrange(1, n + 1):
        result += i
    return result

if __name__ == "__main__":
    print(fact(120))
    print(sum_(120))
    print(script2.fact2(120))
    print(script2.sum2(120))