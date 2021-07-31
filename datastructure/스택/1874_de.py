#1874 스택수열

import sys
n = int(sys.stdin.readline())
stack=[]
res=[]
cur2 = -1
cur1 = 0
for i in range(n):
    num = int(sys.stdin.readline())
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


#간단하게
#굳이 for문 안에서 모든걸 해결하려고 생각하지 말것
# 스택에 for문 넣고 그 후 코드 진행 하는 것