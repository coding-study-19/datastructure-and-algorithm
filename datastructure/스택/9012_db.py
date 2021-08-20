# 백준 | [200]자료구조1 | #9012 | 괄호 | 문자열, 스택

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    a=input()

    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")