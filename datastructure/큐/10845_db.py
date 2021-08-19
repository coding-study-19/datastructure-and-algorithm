# 백준 | [200]자료구조1 | #10845 | 큐 | 큐

import sys
input = sys.stdin.readline

queue = []
cmd_list = []

n = int(input())
for i in range(n):
    cmd_list.append(input().split())

for cmd in cmd_list:
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue) == 0: print(-1)
        else:
            queue.reverse()
            print(queue.pop())
            queue.reverse()
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])