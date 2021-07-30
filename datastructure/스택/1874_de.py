# file = open("C:\\Users\doeoni\OneDrive\doeon\ds_algo\datastructure\스택\input.txt","r",encoding="utf-8")
# n = int(file.readline())
# stack=[]
# result=[]
# cur2 = -1
# cur1 = 0
# for i in range(n):
#     num = int(file.readline())

#     if(num<cur2+1): #stack의 마지막 정수보다 num이 작을 경우 pop 불가능
#         print("NO")
#     else:
#         if(num>cur1): #stack의 누적 정수보다 num이 클 경우
#             push = num-cur1
#             for j in range(1,push+1):
#                 print("+")
#                 stack.append(cur1+j)
#             result.append(stack.pop())
#             print("-")
#             cur1 = num
#         else:
#             result.append(stack.pop())
#             print("-")
#     if stack :
#         cur2 = stack[-1]-1 
#     # print("stack: ",stack)
#     # print("result: ",result)
#     # print("---------------")


file = open("C:\\Users\doeoni\OneDrive\doeon\ds_algo\datastructure\스택\input.txt","r",encoding="utf-8")
n = int(file.readline())
stack=[]
result=[]
res=[]
cur2 = -1
cur1 = 0
for i in range(n):
    num = int(file.readline())
    if(num<cur2+1): #stack의 마지막 정수보다 num이 작을 경우 pop 불가능
        res.clear()
        print("NO")
        break
    else:
        if(num>cur1): #stack의 누적 정수보다 num이 클 경우
            push = num-cur1
            for j in range(1,push+1):
                res.append("+")
                stack.append(cur1+j)
            stack.pop()
            res.append("-")
            cur1 = num
        else:
            stack.pop()
            res.append("-")

    if stack :
        cur2 = stack[-1]-1

for i in range(len(res)):
    print(res[i])




