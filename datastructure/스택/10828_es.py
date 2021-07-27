# 10828 스택
import sys

def stack(cmd):
    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "pop":
        if len(arr) == 0:
            print("-1")
        else:
            print(arr.pop())
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if len(arr) == 0:
            print("1")
        else:
            print("0")
    elif cmd[0] == "top":
        if len(arr) == 0:
            print("-1")
        else:
            print(arr[-1])
    return

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        stack(cmd)
    return

arr = list()
main()
