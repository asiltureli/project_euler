# Mert Asil Tureli
# 17.04.2020
# https://github.com/asiltureli

# ! Conjectured but not proven !
# All prime palindromic numbers must have odd number of digits except "11"
# Thus, considering the low number of digits we are investigating, there are no palindromic primes in our task.

# We might need this multiple times, so just save some code
def find_next_palindrom(current_input):
    pal = 0
    val = int(len(str(current_input))) // 2
    listofstr = list(str(current_input))
    for x in range(0, val):  # Checking current value for being palindrom, pal = len if its palindrom
        if listofstr[x] == listofstr[-(x + 1)]:
            pal += 1

    # If the given number is already a palindrom we just skip this entire step for finding palindrom
    if not (pal == val):
        # Number not Palindrom, finding next lower palindrom
        done = 0
        # If the number acquired from first 3 digits is smaller than the number acquired from last 3 digits,
        # our palindrom starts with our first 3 digits, so we can construct it just by mirroring
        if int("".join(listofstr[0:(val)])) < int("".join([listofstr[-i] for i in range(1, val + 1, 1)])) and not done:
            for index in range(0, val):
                listofstr[-index - 1] = listofstr[index]
                done = 1
        # For some special cases we also must  consider number without their first and last digits
        # We use the algorithm described above with 4 digit number now
        if int("".join(listofstr[1:(val)])) < int("".join([listofstr[-i] for i in range(2, val + 1, 1)])) and not done:
            for index in range(0, val):
                listofstr[-index - 1] = listofstr[index]
                done = 1
        # Same stuff for 4. and 5. digits
        if int("".join(listofstr[2:(val)])) < int("".join([listofstr[-i] for i in range(3, val + 1, 1)])) and not done:
            for index in range(0, val):
                listofstr[-index - 1] = listofstr[index]
                done = 1
        # If not, next lower palindrom starts with input[0:3]-1 e.g. input = 799996, next palindrom must start with 798
        if not done:
            first_3_digits = int("".join(listofstr[0:3])) - 1
            first_3_digits = list(str(first_3_digits))
            for i in range(0, val):
                listofstr[i] = first_3_digits[i]
                listofstr[-1 - i] = first_3_digits[i]
    # Your palindrom is ready
    palipalipali = int("".join(listofstr))
    return palipalipali

# Just a simple function to find prime factors
def get_prime_factors(palindrom):
    prime_list = list()
    # To find prime factors of a number we divide it till square_root (+2 as offset, is optional positiv number, could be 1 too)
    palindrom_temp = palindrom
    for k in range(2, int((palindrom ** (0.5) + 2))):
        # If the number divides our palindrom_temp without rest, its over new prime,
        # divide as long as we can divide it with a rest of 0
        while palindrom_temp % k == 0:
            palindrom_temp = palindrom_temp // k
            prime_list.append(k)
    if palindrom_temp != 1:
        prime_list.append(palindrom_temp)
    return prime_list

# This recursive function allows us to combine prime factors in order to
# find 3 digit multipliers
# We evaluate all combinations as long as they are < 1000
# And we pick one of them and divide our number till we get a new 3 digit number
# Return 1, if number can be written as 3digit * 3digit, 0 else
def get_optimal_multiplier(palindrom,prime_list):
    optimum_list = []
    repeat_list = []
    recursion_exit = []
    def check_found(optimals):
        flag = 0
        for i in range(len(optimals)):
            optimal_2 = palindrom // optimals[i]
            if len(str(palindrom // optimals[i])) == 3 and palindrom == optimals[i]*optimal_2:
                flag = 1
        return flag
    def loop_recursive(factor, liste):
        if liste:
            for loop in range(len(liste)):
                if recursion_exit:
                    break
                if check_found(optimum_list) and optimum_list:
                    recursion_exit.append(1)
                if factor*liste[0] in repeat_list:
                    break
                element= 1
                temp_liste = [x for i,x in enumerate(liste) if i!=len(liste)-loop-1]
                element = element * liste[len(liste)-loop-1]
                if factor*element < 1000:
                    if 99 < factor < 1000 and factor not in optimum_list:
                        optimum_list.append(factor)
                    if 99< element < 1000 and element not in optimum_list:
                        optimum_list.append(element)
                    if factor*element > 99 and factor*element not in optimum_list:
                        optimum_list.append(factor*element)
                    if 99< palindrom/factor < 1000 and palindrom/factor not in optimum_list:
                        optimum_list.append(palindrom//factor)
                    if 99< palindrom/element < 1000 and palindrom/element not in optimum_list:
                        optimum_list.append(palindrom//element)
                    if factor*element * liste[0] < 1000 and not recursion_exit:
                        loop_recursive(factor*element, temp_liste)
                    else:
                        if factor not in repeat_list:
                            repeat_list.append(factor)
    loop_recursive(1, prime_list)
    if recursion_exit:
        return 1
    return 0

result_list = []
t = int(input())
for a0 in range(t):
    n = int(input())-1
    prime_list = list()
    val = int(len(str(n)))//2
    pal = 0
    check = 1
    # Loop till deserved palindrom found
    while check:
        palindrom = find_next_palindrom(n)
        # Now we find the 3 digit products
        # First, we extract all prime factors of our palindrom in order to construct 3 digit products
        prime_list = get_prime_factors(palindrom)
        # If any multiplier of our palindrom has more than 3 digits, we can discard it
        if prime_list[-1] > 999:
            n = palindrom - 1
            continue
        this_is_our_guy = get_optimal_multiplier(palindrom, prime_list)
        # We try to generate 3 digit numbers by multiplying the greatest and smallest prime multipliers
        if this_is_our_guy:
            # It is done
            result_list.append(palindrom)
            check = 0
        else:
            # Check the next palindrom
            n = palindrom-1

[print(result_list[i]) for i in range(len(result_list))]