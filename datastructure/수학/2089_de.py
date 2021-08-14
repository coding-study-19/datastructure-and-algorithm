# 2089 -2진수
import math

dec = int(input())
bin = ""
i=0
sum=0

while(1):
    if sum ==dec:
        print(bin)
        break
    else:
        sum+=math.pow((-2),i)
