# 백준 | [200]자료구조1 | #9093 | 단어뒤집기 | 구현, 문자열

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    word = list(input().split())
    for j in word:
        print(j[::-1], end=' ')
    print()