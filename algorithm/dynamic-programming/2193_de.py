# 2193 이친수
# dp[n] = dp[n-1] + dp[n-2]

N = int(input())
dp = [0,1]
for i in range(2,N+1):
    dp.append(dp[i-1] +dp[i-2])
print(dp[-1])























s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])