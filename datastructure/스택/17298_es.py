# 17298 오큰수
import sys

def nge_timeout():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    result = list()
    isNGE = False

    for i in range(n):
        isNGE = False
        for j in range(i, n):
            if a[i] < a[j]:
                isNGE = True
                result.append(a[j])
                break
        if not isNGE:
            result.append(-1)

    print(" ".join(map(str, result)))
    return

def main():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    idxStack = list()
    result = [-1 for _ in range(n)]

    idxStack.append(0)
    for i in range(1, n):
        while idxStack and A[idxStack[-1]] < A[i]:
            result[idxStack.pop()] = A[i]
        idxStack.append(i)
    
    print(" ".join(map(str, result)))
    return

main()
