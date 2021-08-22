# 11726 2xn 타일링
#dp 점화식 : d[n] = d[n-1] + d[n-2]
# 추가할 수 있는 직사각형의 가로 길이가 1과 2가 전부이므로 가로 길이가 n인 경우를
# 구하려면 n-1길이의 경우에 1길이 직사각형 추가하는 경우 + n-2길이의 경우에 2길이 직사각형을 추가하는 경우
n = int(input())
memo = [None] * (n+1)
def dp(n):
    if n==1: 
        return 1
    elif n==2:
        return 2
    elif memo[n]:
        return memo[n]
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]

print(dp(n))
    
# 내코드 : dp 구현 못함
# n = int(input())

# # 팩토리얼 memozation
# fac=[1,1]
# for i in range(2,n+1):
#     fac.append(i*fac[i-1])

# def calc(n):
#     result = 0
#     arr =[i for i in range(n//2+1)]
#     for num in arr:
#         result+=fac[num+(n-num*2)]//(fac[num]*fac[n-num*2])
#     print(result%10007)

# calc(n)
