# import sys

# num = int(sys.stdin.readline())

# for i in range (num):
#     tmp = sys.stdin.readline()
#     l = list() # 괄호 문자열 분리하기
#     for s in tmp:
#         if(s!="\n"):
#             l.append(s)
#     while(len(l)>1):
#         for j in range (len(l)-1):
#             Continue = False
#             if l[j] == '(' and l[j+1]==')':
#                 del l[j:j+2]
#                 Continue = True
#                 break
#         if (Continue == True):
#             continue
#         else:
#             print("NO") # 와일문의 조건떄문에 괄호 하나 남았을 떄 출력을 못함 / 와일문 조건을 0보다 클때로 바꾸면 for문에서 range가 0이 되어 문제 생김 / 해결책은 여기선 그냥 break하고 밖에서 출력
#             break
#     if(len(l)==0):
#         print("YES")

# del [j], del [j+1] -> j가 del되면 j+1이 j가 되어 del l[j+1]하면 원치않는 결과
# del 하는 방법은 두가지.
# del [j]를 두번 하거나,
# del [j:j+2]으로 슬라이싱을 이용해서 한번에 del하거나

import sys

num = int(sys.stdin.readline())

for i in range (num):
    tmp = sys.stdin.readline()
    l = list() # 괄호 문자열 분리하기
    for s in tmp:
        if(s!="\n"):
            l.append(s)
    while(len(l)>1):
        for j in range (len(l)-1):
            Continue = False
            if l[j] == '(' and l[j+1]==')':
                del l[j:j+2]
                Continue = True
                break
        if (Continue == True):
            continue
        break
    if(len(l)==0):
        print("YES")
    else:
        print("NO")