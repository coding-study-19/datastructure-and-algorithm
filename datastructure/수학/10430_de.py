# 10430 나머지

numList = list(map(int,input().split()))

print((numList[0]+numList[1])%numList[2])
print(((numList[0]%numList[2]) + (numList[1]%numList[2]))%numList[2])
print((numList[0]*numList[1])%numList[2])
print(((numList[0]%numList[2]) * (numList[1]%numList[2]))%numList[2])
