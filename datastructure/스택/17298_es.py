# 17298 오큰수
import sys

def nge_timeout():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    result = list()
    isNGE = False

    # O(N^2)
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


"""
오큰수를 찾지 못한 수를 위해 결과 값을 저장하는 result 리스트를 크기만큼 -1로 초기화한다.
스택에는 인덱스를 넣어주고, 스택의 가장 위에 있는 값을 pop해서 다음 수와 비교한다.
이 비교는 스택에 값이 있을 때만 진행한다.
스택의 가장 위에 있는 인덱스(i)에 해당하는 값보다 오른쪽에 큰 수가 있으면 그 큰 수를 result[i]에 저장한다.
오큰수를 찾은 인덱스는 스택에서 pop해 제거해준다.
"""