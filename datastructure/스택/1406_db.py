# 백준 | [200]자료구조1 | #1406 | 에디터 | 스택, 연결 리스트

import sys
input = sys.stdin.readline

left_stack = []
right_stack = []
string = input().strip()
for i in string:
    left_stack.append(i)

m = int(input())
n = len(left_stack)

for i in range(m):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == 'L' and left_stack != []:
        right_stack.append(left_stack.pop())
    elif cmd_type == 'D' and right_stack != []:
        left_stack.append(right_stack.pop())
    elif cmd_type == 'B' and left_stack != []:
        left_stack.pop()
    elif cmd_type == 'P':
        left_stack.append(command[1])

print("".join(left_stack + right_stack[::-1]))