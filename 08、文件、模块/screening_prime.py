# -*- coding: utf-8 -*-
from math import sqrt


def is_prime(num):
    '''判断一个数是否为素数'''
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

