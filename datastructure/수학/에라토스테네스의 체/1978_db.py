# 백준 | [300]수학1 | #1978 | 소수찾기 | 수학

#에라토스테네스의 체 = 배수를 지워줌
sieve = [True] * 1001
sieve[0], sieve[1] = [False] * 2

i = 2
while i <= 1000:
    if sieve[i]:
        for t in range(i+i, 1001, i):
            if sieve[t]:
                sieve[t] = False
    i += 1

N = int(input())
num = list(map(int, input().rstrip('\n').split(' ')))

result = 0
for i in num:
    if sieve[i]:
        result += 1

print(result)