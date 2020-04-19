# Mert Asil Tureli
# 19.04.2020
# https://github.com/asiltureli

# Pretty simple question which can be solved with formulas
t = int(input().strip())
result_list = []
for a0 in range(t):
    n = int(input().strip())
    result1 = ((n*(n+1))//2)**2
    result2 = ((n*(n+1)*(2*n+1))//6)
    result_list.append(result1 - result2)

for i in range(len(result_list)):
    print(result_list[i])