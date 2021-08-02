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
