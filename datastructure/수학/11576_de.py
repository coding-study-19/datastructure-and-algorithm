#11575 base conversion
import sys

# INPUT
A,B = map(int,input().split())
m = input()
nums = list(map(int,sys.stdin.readline().split()))
nums.reverse()

# A to Dec
dec = 0
for i in range(len(nums)):
    dec+=(A**i)*nums[i]

# Dec to B
decToB=[]
while(1):
    mod = dec%B
    dec //=B
    decToB.append(str(mod))
    if dec==1:
        decToB.append(str(dec))
        break
    elif dec==0:
        break
        
decToB.reverse()

print(" ".join(decToB))

