# file = open("C:\\Users\doeoni\OneDrive\doeon\ds_algo\datastructure\스택\input.txt","r",encoding="utf-8")
# T = int(file.readline())
import sys
T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    # line = file.readline()
    line = sys.stdin.readline()
    line=line.rstrip("\n")
    check = True

    for j in range(len(line)):
       if(line[j]=="("):
           if stack :
                if(stack[-1]=="("):
                    stack.append(line[j])
                else:
                    print("NO")
                    stack.clear()
                    check = False
                    break       
           else:
               stack.append(line[j])    
       else:
           if stack :
                if(stack[-1]=="("):
                    stack.pop()
                else:
                    print("NO")
                    stack.clear()
                    check = False
                    break       
           else:
               print("NO")
               stack.clear()
               check = False
               break
    
    if stack : print("NO")
    elif check==True : print("YES")
    # print("----{0}----".format(i))  
    stack.clear()          

# file.close()

