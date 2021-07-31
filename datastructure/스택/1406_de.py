#1406 에디터
import sys
r_stack = []
l_stack = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())

for _ in range(M):
   command = sys.stdin.readline().split()

   if command[0] =="L":
       if l_stack:
           r_stack.append(l_stack.pop())
       else :
           continue

   elif command[0] == "D":
        if r_stack:
            l_stack.append(r_stack.pop())
        else:
            continue

   elif command[0] == "B":
       if l_stack:
           l_stack.pop()
       else:
            continue

   elif command[0] =="P":
       l_stack.append(command[1])
        
print("".join(l_stack+list(reversed(r_stack))))


#기존 코드
# import sys
# string = list(sys.stdin.readline().rstrip())
# M = int(sys.stdin.readline())
# cur = len(string)-1

# for _ in range(M):
#    command = sys.stdin.readline().split()

#    if command[0] =="P":
#        cur+=1
#        string.insert(cur,command[1])

#    elif command[0] == "B":
#         if cur!=-1:
#             del string[cur]
#             cur-=1
#         else:
#             continue

#    elif command[0] == "D":
#        if cur!=len(string)-1:
#             cur+=1
#        else:
#             continue

#    elif command[0] =="L":
#        if cur!=-1:
#             cur-=1
#        else:
#             continue

# print("".join(string))

# #논리연산자는 타입을 맞춰야 한다
# insert는 list의 index에 값을 넣고 해당 index에 있던 원소는 한칸 뒤로 
# 두개의 리스트 합치기 : 리스트 + 리스트 또는 리스트.extend(리스트)
# list 연산에서는 시간 초과를 고려한다면 insert, del(O(n))보다 pop, append(O(1))를 사용하는 방향으로 생각해보자
# 그래서 인덱스를 일일이 파악해야 하는 커서중심 방법 대신 stack을 나누는 방식 생각