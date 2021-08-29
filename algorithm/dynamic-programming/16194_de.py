# 16194 카드 구매하기2
#점화식 dp[N] = min(dp[i] + p[N-i])
import copy
N = int(input())
dp = [0] + list(map(int,input().split()))
price = dp.copy()

for i in range(2,N+1):
    for j in range(i):
        if dp[i] > dp[j] + price[i-j]:
            dp[i] = dp[j] + price[i-j]
print(dp[-1])
