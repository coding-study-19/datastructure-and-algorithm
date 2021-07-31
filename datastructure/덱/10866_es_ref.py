# 10866 덱
# Dictionary를 사용하여 Switch문 구현
# key값으로 Dictionary에 접근하여 대응되는 value값을 통해 함수 호출
# 출처 : https://roseline124.github.io/algorithm/2019/03/18/Algorithm-190318.html

# 명령어 구현
def push_front(x, deq):
    tmp = [x]
    tmp.extend(deq)
    deq = tmp
    return deq

def push_back(x, deq):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq : 
        print(deq.pop(0))
    else : #빈 리스트 == False
        print(-1)
    
def pop_back(deq):
    if deq :
        print(deq.pop())
    else :
        print(-1)

def size(deq):
    print(len(deq))

def empty(deq) :
    if not deq : 
        print(1)
    else : 
        print(0)
    
def front(deq) :
    if deq :
        print(deq[0])
    else :
        print(-1)
    
def back(deq) :
    if deq :
        print(deq[-1])
    else :
        print(-1)

# 명령어 사전
statements_dict = {
    'push_front' : push_front,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' : pop_back,
    'size' : size,
    'empty' : empty, 
    'front' : front,
    'back' : back
}

# 명령어 처리
N = int(input())

deq = []

for _ in range(N) :
    statement = input().split(" ")
    
    if len(statement) == 1 : 
        command = statement[0]
        statements_dict[command](deq)
    else :
        command, x = statement
        deq = statements_dict[command](x, deq)
