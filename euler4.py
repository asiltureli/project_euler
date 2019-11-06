#!/bin/python3

import sys


t = int(input())
for a0 in range(t):
    n = int(input())
    prime_list = list()
    list1 = list(str(n))
    val = int(len(str(n)))//2
    pal = 0
    for x in range(0,val):
        if list1[x] == list1[-(x+1)]:
            pal += 1

    if pal == val:          # Number Already Palindrom

        for k in range(2, int((n ** (0.5) + 2) // 1)):
            prime = k
            while n % k == 0:
                n = n // k
                prime_list.append(k)
            if n == 1:
                end = 1
                break
        if end == 1:
            print(prime)
        if end == 0:
            print(n)
