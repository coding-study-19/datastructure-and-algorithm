import sys

stack = list()
num = int(sys.stdin.readline())
for i in range (num):
    tmp=sys.stdin.readline().split()
    if(tmp[0]=='push'):
        stack.append(tmp[1])
    elif (tmp[0] == 'pop'):
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif (tmp[0] == 'size'):
        print(len(stack))
    elif (tmp[0] == 'empty'):
        if(len(stack)):
            print(0)
        else:
            print(1)
    elif(tmp[0] == 'top'):
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
            