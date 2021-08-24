# 1463 1로 만들기

#  dp점화식 : d[N] = min(dp[N-1},dp[N//2],dp[n//3])+1
N = int(input())

dp = [0] *(N+1)

for i in range(2,N+1):

    #1을 뺐을 경우 연산 횟수 저장
    dp[i] = dp[i-1]+1

    #i가 2로 나누어 떨어질 경우 i-1의 연산 횟수와 비교해서 최솟값 저장
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

    #i 가 3으로 나누어 떨어질 경우 위의 계산을 통해 얻은 최솟값과 i//3의 연산 횟수와 비교해 최솟값 저장
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[-1])
    


# 내 코드(memozation 구현 안됨)
# from collections import deque
# N = int(input())
# arr=deque()
# arr.append(N)
# count = 0

# def calc(n):
#     # 2또는 3으로 나누어 떨어지는 경우
#     if n%3==0 and n%2==0:
#         arr.append(n//3)
#         arr.append(n//2)
#         arr.append(n-1)
#         return arr

#     # 3으로만 나누어 떨어지는 경우
#     elif n%3==0:
#         arr.append(n//3)
#         arr.append(n-1)
#         return arr

#     #  2로만 나누어 떨어지는 경우
#     elif n%2==0:
#         arr.append(n//2)
#         arr.append(n-1)
#         return arr

#     #이외의 경우
#     else:
#         arr.append(n-1)
#         return arr

# while 1:
#     if min(arr) == 1:
#         break

#     tmp = arr.copy()
#     for num in tmp:
#         calc(num)
#         arr.popleft()

#     count+=1
# print(count)

# 내코드 2
# 재귀 횟수의 한계 때문에 실패
# def calc(n):
#     if arr[n]:
#         return arr[n]

#     if n==1:
#         return 0

#     # 2또는 3으로 나누어 떨어지는 경우
#     elif n%3==0 and n%2==0:
#         arr[n] = min(calc(n//3),calc(n//2),calc(n-1)) + 1
#         return arr[n]

#     # 3으로만 나누어 떨어지는 경우
#     elif n%3==0:
#         arr[n] = min(calc(n//3),calc(n-1)) +1
#         return arr[n]

#     #  2로만 나누어 떨어지는 경우
#     elif n%2==0:
#         arr[n] = min(calc(n//2),calc(n-1)) + 1
#         return arr[n]

#     #이외의 경우
#     else:
#         arr[n] = calc(n-1)+1
#         return arr[n]


