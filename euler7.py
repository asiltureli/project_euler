# Mert Asil Tureli
# 19.04.2020
# https://github.com/asiltureli

# Idea: create a list of all primes till input n_1
# 1) If new input n_2 is greater than n_1 expand the list till n_2
# 2) If new input n_2 is smaller than n-1 search the list for the result

t = int(input().strip())
prime_list=[2]
result_list=[]
for a0 in range(t):
    n = int(input().strip())
    # Case 2
    if n <= len(prime_list):
        result_list.append(prime_list[n-1])
        continue
    # Case 1
    else:
        prime_flag = 1
        current_prime = prime_list[-1] + 1
        while len(prime_list)<n and prime_flag:
            for loop in range(len(prime_list)):
                if current_prime % prime_list[loop] == 0:
                    prime_flag = 0
                    break
            if prime_flag == 1:
                prime_list.append(current_prime)
            current_prime += 1
            prime_flag = 1
        result_list.append(prime_list[n-1])

[print(result_list[i]) for i in range(len(result_list))]
