# 백준 | [303]수학1 (참고) | #11653 | 소인수분해 | 수학

n = int(input())
arr = []

if n == 1:
    print(' ')

i = 2
while (n!=1):
    if n%i == 0:
        arr.append(i)
        n //= i
    else:
        i += 1

for i in arr:
    print(i)