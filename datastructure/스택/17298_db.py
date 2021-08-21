# 백준 | [201]자료구조1 | #17298 | 오큰수 | 스택

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

stack = []
result = [-1] * N

for i in range(N):
    while stack and num_list[stack[-1]] < num_list[i]:
        result[stack.pop()] = num_list[i]
    stack.append(i)

print(*result)