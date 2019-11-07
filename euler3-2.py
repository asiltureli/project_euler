#!/bin/python3

import sys
import math


t = int(input())
for a0 in range(t):
    n = int(input())
    end = 0
    for k in range(2, int((n**(0.5) + 2) // 1)):
        prime = k
        while n%k == 0:
            n = n//k
        if n == 1:
            end = 1
            break
    if end == 1:
        print(prime)
    if end == 0:
        print(n)
