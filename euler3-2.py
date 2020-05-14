#!/bin/python3

import sys
import math

# To find the highest prime factor, we need to find
# prime factors building the number
# In order to achieve this we must divide our number to 
# all prime factors till n^^0.5, since number must have at least one prime factor k_1<n^^0.5
# for a prime factor k_2>n^^0.5

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
