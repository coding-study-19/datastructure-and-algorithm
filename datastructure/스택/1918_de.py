# 1935 후위 표기식
import sys
from collections import deque

operation = deque(list(sys.stdin.readline().rstrip()))
opStack=[]

#인덱스 연산을 할 땐 언제나 범위 에러 잡기

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

