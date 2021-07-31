#9012 괄호
import sys
T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    line = sys.stdin.readline()
    line=line.rstrip("\n") #문자열 마지막 개행 제거.문자를 일일이 확인해서 필요. 
    check = True

    for j in range(len(line)): #문자 하나씩 체크
       if(line[j]=="("): # 열림 입력 시 스택 empty여부 체크 
           if stack :
                if(stack[-1]=="("):
                    stack.append(line[j])
                else:
                    print("NO")
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
                    check = False
                    break       
           else:
               print("NO")
               check = False
               break
    
    if stack : print("NO") #검사 후 스택 !=empty => 오류
    elif check==True : print("YES") #stack == empty인데 틀린 경우를 거르기 위함
    stack.clear()    


# 문자를 일일이 체크하는 것 보단 처음부터 for 문자 in 문자열로.
# 굳이 스택을 쓰지 않더라도 count를 해서 성능 높일 수 있다.    
#파이썬스러운(=간결한) 코드 지향. 

#새롭게 알게된 것
#여러줄로 이루어진 문장을 읽을 때 문장의 맨 마지막에 개행이 들어감
#이를 제거하는 코드.
# line = sys.stdin.readline()
#     line=line.rstrip("\n") 
#     check = True