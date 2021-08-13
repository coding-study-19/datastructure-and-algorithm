# 백준 _ [200]자료구조1 _ #9012 _ 괄호 _ 문자열, 스택

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