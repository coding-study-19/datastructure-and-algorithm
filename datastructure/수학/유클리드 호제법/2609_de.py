# 2609 최대공약수와 최소공배수

#반례가 은근 많아 생각보다 풀기 까다로웠던 문제..
#이렇게 반례가 많을 경우는 하나씩 적어가며 대입해보자. 머릿속으로 생각하니 헷갈림
numList=list(map(int,(input().split())))
minNum=0

for i in range(1,max(numList)+1):
    if numList[0] == numList[1]:
        minNum = numList[0]
        maxNum = numList[0]
        break

    elif numList[0]%i==0 and numList[1]%i==0 and minNum<i:
            minNum=i

maxNum = minNum * (numList[0]//minNum) * (numList[1]//minNum)

print(minNum)
print(maxNum)
