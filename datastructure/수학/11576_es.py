# 11576 Base Conversion
import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    ten = 0
    answer =[]
    for i in range(m):
        ten += arr[-1] * (A**i)
        arr.pop(-1)
    while ten != 0:
        answer.append(str(ten % B))
        ten //= B

    print(' '.join(answer[::-1]))
    return

main()
