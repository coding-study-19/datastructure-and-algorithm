# 백준 | [303]수학1 (참고) | #2745 | 진법 변환 | 수학

N, B = input().split()
B = int(B)

result = 0
power = 0

for i in N[::-1]:
    if i.isdigit(): t = int(i)
    else: t = ord(i) - 55

    result += (t * (B ** power))
    power += 1

print(result)