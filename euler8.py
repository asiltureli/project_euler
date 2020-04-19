# Mert Asil Tureli
# 19.04.2020
# https://github.com/asiltureli

# Multiply K digits with stride 1 till we face a zero
# If we face zero, skip that and start to multiplying K digits again

result_list = []
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    str_list = list(num)
    int_list = [int(x) for x in str_list]
    if k == 1:
        result_list.append(max(int_list))
        continue
    step = 0
    save_flag = 0
    skip_idx = 0
    candidate_list = []
    while step < n - k + 1:
        candidate = 1
        zero_flag = 0
        for loop in range(step,step+k):
            if int_list[loop] == 0:
                zero_flag = 1
                skip_idx = loop
                break
            else:
                candidate *=  int_list[loop]
        if zero_flag:
            step = loop +1
        else:
            candidate_list.append(candidate)
            step += 1

    if not candidate_list:
        result_list.append(0)
    else:
        result_list.append(max(candidate_list))

[print(result_list[i]) for i in range(len(result_list))]