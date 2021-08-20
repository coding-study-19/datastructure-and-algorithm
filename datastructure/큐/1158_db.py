# 백준 | [200]자료구조1 | #1158 | 요세푸스 문제 | 큐

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]

answer = []
num = 0

for t in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)
    answer.append(str(arr.pop(num)))

print("<", ", ".join(answer)[:], ">", sep='')