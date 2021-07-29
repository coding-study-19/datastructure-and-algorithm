# 10845 큐
import sys

def queue(cmd):
    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "pop":
        if arr == []:
            print("-1")
            return
        print(arr[0])
        del arr[0]
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
        queue(cmd)
    return

arr = list()
main()
