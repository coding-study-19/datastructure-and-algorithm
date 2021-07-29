# 1874 스택 수열
import sys

def main():
    n = int(sys.stdin.readline())
    stack = list()
    result = list()
    cnt = 0
    
    for _ in range(n):
        x = int(sys.stdin.readline())

        while x > cnt:
            cnt += 1
            stack.append(cnt)
            result.append("+")

        if x == stack[-1]:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            return

    for op in result:
        print(op)
    return

main()
