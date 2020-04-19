def get_primes(limit):
    # Find all primes till limit
    prime_list = [2]
    limit = limit + 1
    for num_to_try in range(3, limit):
        # If the number divides our palindrom_temp without rest, its over new prime,
        # divide as long as we can divide it with a rest of 0
        element = num_to_try
        for current_prime_idx in range(len(prime_list)):
            while not element % prime_list[current_prime_idx]:
                element = element // prime_list[current_prime_idx]
        if element != 1:
            prime_list.append(num_to_try)
    return prime_list
def get_squares(prime_list, limit):
    for loop in range(len(prime_list)):
        current_number = prime_list[loop]
        sqr_temp = prime_list[loop]
        flag = 0
        while sqr_temp <= limit:
            flag = 1
            sqr_temp = sqr_temp*current_number
        if flag:
            prime_list[loop] = sqr_temp//current_number
    return prime_list
t = int(input().strip())
result_list = []
for a0 in range(t):
    n = int(input().strip())
    if n == 1 :
        result_list.append(1)
        continue
    prime_list = []
    prime_list = get_primes(n)
    list_mult = []
    list_mult = get_squares(prime_list, n)
    result = 1
    for x in range(len(list_mult)):
        result *= list_mult[x]
    result_list.append(result)

for y in range(len(result_list)):
    print(result_list[y])