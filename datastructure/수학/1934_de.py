# 1934 최소공배수
import sys
T = int(input())
#초기화 주의..
for i in range(T):
    minNum=0
    numList = list(map(int,sys.stdin.readline().split()))
    if numList[0] == numList[1]:
        print(numList[0])

    else:
        for i in range(1,(max(numList)//2)+1):
            if numList[0]%i==0 and numList[1]%i==0 and i>minNum:
                minNum=i
        print(minNum * (numList[0]//minNum) * (numList[1]//minNum))

        


