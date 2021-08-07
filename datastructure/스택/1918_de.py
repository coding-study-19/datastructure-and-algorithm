# 1935 후위 표기식
import sys
from collections import deque

operation = deque(list(sys.stdin.readline().rstrip()))
opStack=[]

#인덱스 연산을 할 땐 언제나 범위 에러 잡기
#굳이 popleft를 안하고 바로 출력해도 되는 부분이었음. 출력하고 뒤로 돌아가지 않으니 popleft와 동일하 효과
for i in range(len(operation)):
    if operation[0].isalpha():
        print(operation.popleft(), end="")

    elif operation[0] == "+" or operation[0] == "-":
        while opStack and opStack[-1]!="(":
            print(opStack.pop(), end="")
        opStack.append(operation.popleft())

    elif operation[0] == "*" or operation[0] == "/":
        while opStack and (opStack[-1] == "*" or opStack[-1] == "/"):
            print(opStack.pop(), end="")
        opStack.append(operation.popleft())

    else:
        if operation[0] == "(":
            opStack.append("(")
            operation.popleft()

        else:
            operation.popleft()
            while opStack:
                if(opStack[-1]=="("):
                    opStack.pop()
                    break
                print(opStack.pop(), end="")
while opStack:
    print(opStack.pop(), end="")

