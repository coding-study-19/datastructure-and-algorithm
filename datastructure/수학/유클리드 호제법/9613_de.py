#9613 GCD합
import sys
t = int(input())

for _ in range(t):
    numList = list(map(int,sys.stdin.readline().split()))
    result = 0

    for i in range(1,numList[0]+1):
        for j in range(2,numList[0]+1):
            if i == j or j<i: continue
            num1 = max(numList[i],numList[j])
            num2 = min(numList[i],numList[j])
            #유클리드 호제법
            while(1):
                mod = num1 % num2
                if mod ==0:
                    result+=num2
                    break
                num1 = num2
                num2 = mod
    print(result)




                


