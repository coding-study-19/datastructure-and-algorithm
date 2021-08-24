# 9095 1 2 3 더하기
# dp 점화식 : d[N] = d[N-1] +d[N-2] + d[n-3]

def dp(n,memo):
    if memo[n]:
        return memo[n]
    else:
        memo[n] = dp(n-1,memo) + dp(n-2,memo) + dp(n-3,memo)
        return memo[n]

def main():
    T = int(input())
    memo = [0,1,2,4]+[None]*7
    for _ in range(T):
        n = int(input())
        print(dp(n,memo))

main()

