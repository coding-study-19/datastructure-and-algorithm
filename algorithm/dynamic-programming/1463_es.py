# 1463 1로 만들기
import sys

# dynamic programming
def make_to_one(n):
    memo = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        memo[i] = memo[i-1] + 1 # n-1을 먼저 해줘야 최소값이 나옴 (반례 : 10)
        if i % 2 == 0 and memo[i] > memo[i//2] + 1:
            memo[i] = memo[i//2]+1
        if i % 3 == 0 and memo[i] > memo[i//3] + 1:
            memo[i] = memo[i//3] + 1
    return memo[n]

def main():
    n = int(sys.stdin.readline())
    print(make_to_one(n))
    return

main()

"""
점화식 : dp(N) = min ( dp(N//3)+1, dp(N//2)+1 , dp(N-1)+1 )

[출처] https://infinitt.tistory.com/247
"""