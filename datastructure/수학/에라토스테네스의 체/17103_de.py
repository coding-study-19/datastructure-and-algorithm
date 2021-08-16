# 17103 골드바흐 파티션
import sys
max = 1000000
array = [True] *max
end = int(max**0.5)+1
for i in range(2,end):
    if array[i]:
       for j in range(i+i,max,i):
           if array[j]:
               array[j] = False

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0

    for i in range(2,N//2+1):
        if array[i] and array[N-i]:
            count+=1    
    print(count)
