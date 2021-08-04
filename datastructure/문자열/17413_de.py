# 17413 단어뒤집기2
import sys
from collections import deque

sentence = list(sys.stdin.readline().rstrip())
i = 0
# start = 0

while i<len(sentence):
    if sentence[i] == "<":
        while sentence[i] != ">":
            i+=1
    elif sentence[i].isalnum():
        start = i
        while i<len(sentence) and sentence[i].isalnum():
            i+=1
        tmp = sentence[start:i]
        tmp.reverse()
        sentence[start:i] = tmp
    else:
        i+=1
print("".join(sentence))

#절대로 반복문 안에 slice와 같은 시간 복잡도 큰 연산 넣지 말자
#저번부터 괄호 문제를 복잡하게 생각함. 스택자체를 다루려고 하지 말고 인덱스를 이용해 필요 없는 부분을 날릴 수 있다.
# reverse와 slice를 이용하면 스택의 특정 부분만 수정 가능하다!
#list는 문자열을 글자로 쪼개 리스트로 만들어주고 []는 문자열을 통으로 리스트로 만든다
# isalnum 을 이용해 공백과 문자를 구분 가능하다! isalnum(알파벳이나 숫자) : True

#기존 코드
#문자열을 일일이 뒤집어서 코드가 길어짐 -> slice와 reverse로 해결!
# sentence = [word for word in sys.stdin.readline().rstrip()]
# stack = deque()
# change_stack=[]
# idx=0

# while(idx<len(sentence)):
#     stack.append(idx)

#     if sentence[stack[-1]] == "<":
#         if len(stack)>1:
#             stack.pop()
#             stackIdx = stack[0]
#             while stack or change_stack:
#                 if stack:
#                     if sentence[stack[0]] ==" ":
#                         stack.popleft()
#                         while change_stack:
#                             sentence[stackIdx] = change_stack.pop()
#                             stackIdx+=1
#                         stackIdx+=1
#                     else:
#                         change_stack.append(sentence[stack.popleft()])
#                 else:
#                     sentence[stackIdx] = change_stack.pop() 
#                     stackIdx+=1

#     elif sentence[stack[-1]] == ">":
#         stack.clear()

#     elif idx == len(sentence)-1:
#         if stack:
#             stackIdx = stack[0]
#             while stack or change_stack:
#                 if stack:
#                     if sentence[stack[0]] ==" ":
#                         stack.popleft()
#                         while change_stack:
#                             sentence[stackIdx] = change_stack.pop()
#                             stackIdx+=1
#                         stackIdx+=1
#                     else:
#                         change_stack.append(sentence[stack.popleft()])
#                 else:
#                     sentence[stackIdx] = change_stack.pop() 
#                     stackIdx+=1
#     idx+=1

# print("".join(list(map(str,sentence))))