# 백준 | [200]자료구조1 | #10828 | 스택 | 스택

import sys
input = sys.stdin.readline

stack_list = []
n = int(input())

for x in range(n):
    command = list(input().split())

    if command[0] == 'push':
        stack_list.append(command[1])
    elif command[0] == 'pop':
        if len(stack_list) == 0: print(-1)
        else: print(stack_list.pop())
    elif command[0] == 'size':
        print(len(stack_list))
    elif command[0] == 'empty':
        if len(stack_list) == 0: print(1)
        else: print(0)
    elif command[0] == 'top':
        if len(stack_list) == 0: print(-1)
        else: print(stack_list[-1])
