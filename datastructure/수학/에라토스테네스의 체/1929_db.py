# 백준 | [300]수학1 | #1929 | 소수구하기 | 수학

m, n = list(map(int, input().rstrip('\n').split(' ')))

n += 1
prime = [True] * n

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(2*i, n, i):
            prime[j] = False

for i in range(m, n):
    if (i > 1) and (prime[i] == True):
        print(i)