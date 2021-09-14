# 백준 | [301]수학1 (연습) | #17087 | 숨바꼭질 6 | 유클리드호제법

import math
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

ck = []
for i in A:
    ck.append(abs(i - S))

ans = ck[0]
for i in range(1, N):
    ans = math.gcd(ck[i], ans)

print(ans)
