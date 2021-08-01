# 17299 오등큰수
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    A = list(sys.stdin.readline().split())

    stack = []
    cnt = Counter(A)
    s = [[cnt[num], int(num)] for num in A]
    result = [-1 for _ in range(n)]
    stack.append(0)

    i = 1
    while stack and i < n:
        while stack and s[stack[-1]][0] < s[i][0]:
            result[stack[-1]] = s[i][1]
            stack.pop()

        stack.append(i)
        i += 1

    print(" ".join(map(str, result)))

main()
