# 2748 피보나치 수 2
import sys

memo = [0 for _ in range(101)] # 0~100

# recursive O(2^N)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# top-down dynamic programming O(N)
def topdown_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = topdown_fibo(n-1) + topdown_fibo(n-2)
        return memo[n]

# bottom-up dynamic programming O(N)
def bottomup_fibo(n):
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def main():
    n = int(sys.stdin.readline())
    print(fibonacci(n))
    print(topdown_fibo(n))
    print(bottomup_fibo(n))
    return

main()

"""
top-down 채점 소요 시간 : 80ms
bottom-up 채점 소요 시간 : 88ms
"""