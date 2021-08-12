# 1676 팩토리얼 0의 개수
import sys

def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * factorial(n - 1)

def runtime_error_main():
    n = int(sys.stdin.readline())

    factN = factorial(n)
    cnt = 0
    while factN % 10 == 0:
        cnt += 1
        factN //= 10

    print(cnt)
    return

def main():
    n = int(sys.stdin.readline())
    print(n//5 + n//25 + n//125)
    return

main()

"""
팩토리얼로 얻을 수 있는 수를 인수 분해 했을때, 0이 늘어나는 순간은 10(2x5)가 곱해지는 순간이다.
따라서 5의 개수를 찾으면 쉽다.
"""