#17299 오등큰수
import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))

stack=[]
count =[0]*(max(A)+1) #이게 포인트 N과 상관 없이 A안의 원소는 겁내 큰수도 가능하기 때문에 count를 이렇게 설정해줘야 한다.
answer=[0]*N

#count 해줌(이게 포인트!) for 문을 분리하였기 때문에 O(N)
for i in range(N):
    count[A[i]]+=1

#오큰수
for i in range(N):
    while stack and count[A[stack[-1]]] < count[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)
while stack:
    answer[stack.pop()] = -1
print(" ".join(list(map(str,answer))))
