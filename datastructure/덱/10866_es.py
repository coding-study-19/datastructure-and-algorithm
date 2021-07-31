# 10866 덱
import sys

def deque(cmd):
    if cmd[0] == "push_front":
        arr.insert(0, int(cmd[1]))
    elif cmd[0] == "push_back":
        arr.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if arr == []:
            print("-1")
            return
        print(arr.pop(0))
    elif cmd[0] == "pop_back":
        if arr == []:
            print("-1")
            return
        print(arr.pop())
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if arr == []:
            print("1")
        else:
            print("0")
    elif cmd[0] == "front":
        if arr == []:
            print("-1")
            return
        print(arr[0])
    elif cmd[0] == "back":
        if arr == []:
            print("-1")
            return
        print(arr[-1])
    return

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        deque(cmd)
    return

arr = list()
main()
