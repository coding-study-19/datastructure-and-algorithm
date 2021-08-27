# 11052 카드 구매하기

N = int(input())
d=[0]*(N+1)
price=[0] + list(map(int,input().split()))
d[1] = price[1]

for i in range(2,N+1):
    for j in range(i+1):
        if d[i] < d[j] + price[i-j]:
            d[i] = d[j] + price[i-j]
print(d[-1])
