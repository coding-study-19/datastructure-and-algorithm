# 11656 접미사 배열
word = input()
wordList=[]
for i in range(len(word)):
    wordList.append(word[i:])

wordList.sort()
for each in wordList:
    print(each)
#정렬엔 sort를 쓰자..! 코드 짜는데 개힘들었는데..머리가 나쁘면 몸이 고생^^

#로직:
# answer을 스택으로 que를 deque로 만들어서 큐의 맨 앞 원소와 answer의 맨 마지막 원소끼리 비교한다.
#그렇게 비교해서 큐 원소 순위 < answer원소 순위 일 경우 answer에 큐 popleft()를 append해주고
# 큐 원소 순위 >  answer원소 순위 일 경우 answer를 pop하면서 더 큰 순위의 answer원소가 나올 때까지
# 비교해준다. 큐 원소 순위 ==  answer원소 순위 일 경우 원소 안의 문자를 하나씩 비교한다. 
# 그럼 저절로 정렬이 된다
# 맞음
# if not answer:
#     answer.append(que.popleft())

# else:
#     # 맞음
#     if ord(answer[-1][0]) < ord(que[0][0]):
#         answer.append(que.popleft())
    
#     elif ord(answer[-1][0]) > ord(que[0][0]):
#         que.append(answer.pop())

#         while answer:
#             #answer의 마지막 원소의 우선순위 < que의 우선순위
#             if ord(answer[-1][0]) > ord(que[0][0]):
#                 que.append(answer.pop())

#             #answer의 마지막 원소의 우선순위 == que의 우선순위
#             elif ord(answer[-1][0]) == ord(que[0][0]):
#                 idx=1
#                 while answer:
#                     #각 원소의 두번째 글자부터 비교 시작
#                     if ord(answer[-1][idx]) > ord(que[0][idx]):
#                         que.append(answer.pop())
#                         break
#                     elif ord(answer[-1][idx]) == ord(que[0][idx]):
#                         idx+=1
#                     else: 
#                         answer.append(que.popleft())
#                         break

#             #answer의 마지막 원소의 우선순위 > que의 우선순위
#             else:
#                 answer.append(que.popleft())
#                 break


#     elif ord(answer[-1][0]) == ord(que[0][0]):
#         #우선순위 같을 경우
#         idx=1
#         while answer:
#             #각 원소의 두번째 글자부터 비교 시작
#             if ord(answer[-1][idx]) > ord(que[0][idx]):
#                 que.append(answer.pop())
#                 break
#             elif ord(answer[-1][idx]) == ord(que[0][idx]):
#                 idx+=1
#             else: 
#                 answer.append(que.popleft())
#                 break
