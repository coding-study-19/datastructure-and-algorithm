# 2xn 타일링 2
# 점화식 : d{N} = 2d[N-2] + d[N-1]

n = int(input())
memo = [0,1,3]+[None]*(n-2)

for i in range(3,n+1):
    memo[i] = memo[i-1] + 2*memo[i-2]
print(memo[n]%10007)


#recursionError
# memo = [None]*(n+1)
# def calc(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 3
#     elif memo[n]:
#         return memo[n]   
#     memo[n] = calc(n-1) + 2*calc(n-2)
#     return memo[n]

# print(calc(n))