#17928 오큰수
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
stack=[0]
answer=[-1]*N
for i in range(1,N):
    while stack and A[stack[-1]]<A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(" ".join(list(map(str,answer))))

# O(N)에 가까움
# 기존 코드처럼 요소를 n번씩 비교하며 순회하는 연산 대신 시간 복잡도를 낮추기 위해 요소를 하나씩 비교하는 연산을 수행한다.
# 왼쪽 요소 > 오른쪽 요소일 경우 왼쪽 요소의 인덱스를 스택에 누적한다.
# 왼쪽 요소 < 오른쪽 요소일 경우 왼쪽 요소를 pop하며 차례로 비교한다.

# 입력받은 스택의 순서와 정답으로 출력될 스택의 순서가 일치해야 할 때 나는 보통 요소 자체를 스택에 넣고 인덱스를 찾아 재배치
# 하는 방법을 생각하는데, 이것보다 요소의 인덱스를 저장하면 별도의 연산 필요 없이 인덱스별로 요소를 배치할 수 있다. 


# 기존 코드
# res=[-1]*N
# for i in range(N):
#     index = i+1
#     for _ in range(index,N):
#             if A[i]<A[index]:
#             res[i] = A[index]
#             break
#         else:
#             index+=1
# print(" ".join(list(map(str,res))))  
# 시간 복잡도 : O(N^2) => 너무 느림
# list comprehension
# bigNumList = [n for n in rlist if n > A[i]]






