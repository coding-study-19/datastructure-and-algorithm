# 백준 | [303]수학1 (참고) | #11576 | Base Conversion | 수학

import sys
input = sys.stdin.readline

# 입력
a, b = map(int, input().rstrip('\n').split( ))
m = int(input())
arr = list(map(int, input().rstrip('\n').split( )))

ten = 0
answer =[]

# a진법 -> 10진법
for i in range(m):
    ten += arr[-1] * (a**i)
    arr.pop(-1)

# 10진법 -> b진법
while ten != 0:
    answer.append(str(ten % b))
    ten = ten // b

#출력
print(' '.join(answer[::-1]))