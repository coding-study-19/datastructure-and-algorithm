# 1,2,3 더하기 5
# 점화식 dp[N] = (dp[N-1]-sub[1][1]) + (dp[N-2]-sub[2][2]) + (dp[N-3]-sub[3][3])

T = int(input())
sub = [0,[0,1,1,1],[0,0,1,0],[0,1,0,0]]
dp = [0,1,1,3]
for _ in range(T):
    n = int(input())
    for i in range(len(dp),n+1):
        tmp = [0,dp[i-1]-sub[1][1],dp[i-2]-sub[2][2],dp[i-3]-sub[3][3]]
        sub[1],sub[2],sub[3] = tmp,sub[1],sub[2]
        dp.append(sum(sub[1])%1000000009)
    print(dp[n])


# 다른 풀이
# 나는 N과 N의 부분집합을 각각 dp,sub에 담아 관리했는데 
# 이 코드는 함께 관리함 dp[N][sub]
mod = 1000000009
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,100001):
    dp[i][0] = dp[i-1][1]%mod + dp[i-1][2]%mod
    dp[i][1] = dp[i-2][0]%mod + dp[i-2][2]%mod
    dp[i][2] = dp[i-3][0]%mod + dp[i-3][1]%mod






    

