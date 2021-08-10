# 1929 소수 구하기
import math

numList = list(map(int,input().split()))
start = numList[0]
end = numList[1]+1

for num in range(start, end):
    isPrime = True
    # 1 예외처리
    if num == 1:
        isPrime = False
        continue
    #에라토스테네스의 접근
    for j in range(2, int(math.sqrt(num)+1)):
        if num%j==0:
            isPrime = False
            break

    if isPrime:
        print(num)
