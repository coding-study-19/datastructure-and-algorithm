# 백준 | [203]자료구조1 | #1918 | 후위 표기식 | 스택

import sys
input = sys.stdin.readline

expression = input()

stack = []
ans = ""

for s in expression:
    if s == '+' or s == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        ans += s

while stack:
    ans += stack.pop()

print(ans)