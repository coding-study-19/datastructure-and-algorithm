#10828 스택
import sys
n = int(sys.stdin.readline())
stack=[]

for i in range(n):
    command_line = sys.stdin.readline().split()
    if(command_line[0]=="push"):
        stack.append(command_line[1])
    elif(command_line[0]=="pop"):
        if stack :
            print(stack.pop())
        else:
            print('-1')
    elif(command_line[0]=="size"):
        print(len(stack))
    elif(command_line[0]=="empty"):
        if stack : 
            print('0')
        else : 
            print('1')
    elif(command_line[0]=="top"):
        if stack:
            print(stack[-1])
        else:
            print('-1')