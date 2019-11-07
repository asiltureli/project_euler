#!/bin/python3

import sys


t = int(input())
for a0 in range(t):
    n = int(input())
    prime_list = list()
    list1 = list(str(n))
    factor_list = [1,1]
    val = int(len(str(n)))//2
    pal = 0
    check = 1
    while check:
        factor_list = [1, 1]
        val = int(len(list1)) // 2
        pal = 0
        end = 0
        prime_list = list()
        for x in range(0,val):      # Checking current value for being palindrom, pal = len if its palindrom
            if list1[x] == list1[-(x+1)]:
                pal += 1
        if not(pal == val):          # Number not Palindrom, finding next low palindrom
            done = 0
            if int("".join(list1[0:(val)])) <  int("".join(list1[-(val):])):
                for index in range(0, val):
                    list1[-index - 1] = list1[index]
                    done = 1
            if not(int(list1[val - 1]) == 0) and not done :
                list1[val-1] = str(int(list1[val-1])-1)
            elif int(list1[val - 1]) == 0 and not (int(list1[val - 2]) == 0) and not done:
                list1[val-2:val] = str(int("".join(list1[(val-2):(val)]))-1)
            elif val - 3 >= 0 and int(list1[val - 2]) == 0 and not (int(list1[val - 3]) == 0) and not done:
                list1[val-3:val] = str(int("".join(list1[(val - 3):(val)]))-1)
            if not done:
                for index in range(0,val):
                    list1[-index-1] = list1[index]
            #if not(int("".join(list1[0:(val)])) > int("".join(list1[-(val):]))):
            #new = int("".join(list1))
            #if  new > temp:
             #   list1[val-1] =
        n = int("".join(list1))
        for k in range(2, int((n ** (0.5) + 2) // 1)):
             prime = k
             while n % k == 0:
                n = n // k
                prime_list.append(k)
             if n == 1:
                end = 1
                break
        if end == 0:
            pal = 0
            list1[val-1] = str(int(list1[val-1])-1)
            list1[val] = str(int(list1[val-1])-1)
            continue


        factor_list[0] = prime_list[-1]
        del prime_list[-1]
        factor_list[1] = prime_list[-1]
        del prime_list[-1]
        while prime_list:
            factor_list[0] = factor_list[0]*prime_list[0]
            del prime_list[0]
            if prime_list:
                factor_list[1] *= prime_list[0]
                del prime_list[0]

        if (len(str((factor_list[0]))) == 3 and len(str((factor_list[1]))) == 3):
            print(int("".join(list1)))
            check = 0
        else:
            list1[val-1] = str(int(list1[val-1])-1)


