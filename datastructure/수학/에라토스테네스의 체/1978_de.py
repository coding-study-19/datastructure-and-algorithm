#1978 소수 찾기
import math
N = int(input())
numList=list(map(int,(input().split())))
end = int(math.sqrt(max(numList))+1)
result = 0

for num in numList:
    isPrime = True
    # 1예외처리
    if num == 1 :
        isPrime = False
        continue

    #에라토스테네스의 접근
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        result+=1
print(result)



