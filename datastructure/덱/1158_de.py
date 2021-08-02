# #1158 요세푸스 문제
import sys
import copy
from collections import deque
N, K = map(int, sys.stdin.readline().split())

rqueue = deque([i+1 for i in range(N)])
lqueue=deque([])
result=[]
cnt=0

while(1):
    if rqueue:
        lqueue.append(rqueue.popleft())
        cnt+=1
        if(cnt==K):
            result.append(lqueue.pop())
            cnt=0
    else:
        if lqueue:
            rqueue = copy.copy(lqueue)
            lqueue.clear()
        else:
            break
print("<{}>".format(", ".join(list(map(str,result)))))

#join함수는 문자열 리스트만 취급하기 때문에 정수 리스트는 문자열 리스트로 변환해야 함
# 객체 복사 시 주소가 참조되는 것 =>copy 사용으로 해결

# 리스트 순환은 나머지 연산으로 구현할 수 있다.
# N,K = map(int,input().split())
# arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

# answer = []   # 제거된 사람들을 넣을 배열
# num = 0  # 제거될 사람의 인덱스 번호

# for t in range(N):
#     num += K-1  
#     if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
#         num = num%len(arr)
 
#     answer.append(str(arr.pop(num)))
# print("<",", ".join(answer)[:],">", sep='')
