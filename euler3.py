#!/bin/python3

import sys


t = int(input())
prime_list = list()
prime_list.append(2)
prime_list.append(3)
prime_list.append(5)
prime_list.append(7)
prime_list.append(11)
for a0 in range(t):
    n = long(input())
    for k in range(0, int((n**(0.5) + 2) // 1)):
        actual = prime_list[k]
        end = 0
        while n % prime_list[k] == 0:
            n = n // prime_list[k]
            if n == 1:
                break
        #while n % prime_list[k+1] == 0:
        #    n = n // prime_list[k+1]
        #    if n == 1:
        #        actual = prime_list[k+1]
        #        break
        #while n % prime_list[k + 2] == 0:
        #    n = n // prime_list[k + 2]
        #    if n == 1:
        #        actual = prime_list[k + 2]
        #        break
        if n == 1:
             break
        if n**(0.5)// 1 == n**(0.5)/ 1:
            ind =  int((n**(0.5) + 1))
        else:
            ind = int((n**(0.5) + 2)//1)
            if ind < actual:
                end = 1
        for l in range(prime_list[-1], ind+1, 2):
            cont = 0
            for pr in range(0, len(prime_list)):
                if l % prime_list[pr] == 0:
                    cont = 1
                    break
            if cont == 0:
                prime_list.append(l)
                if l == int((n ** (0.5) + 1) // 1):
                    end = 1
                break
            if l == int((n**(0.5) + 1) // 1) or l == int((n**(0.5)) // 1) :
                end = 1
                break
        if end == 1:
            break
    if end == 1:
        print(n)
    if n == 1:
        print(actual)





