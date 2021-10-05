# 백준 | [303]수학1 (참고) | #11005 | 진법 변환 2 | 수학

n, b = map(int, input().split( ))
arr = []

while n >= b:
    arr.append(n % b)
    n //= b

arr.append(n%b)
if n//b > 0:
    arr.append(n//b)

for i in arr[::-1]:
    if i >= 10:
        print(chr(i+55), end='')
    else:
        print(i, end='')