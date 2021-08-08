# 1918 후위 표기식
import sys

def main():
    a = sys.stdin.readline().strip()
    stack = [] # 연산자 스택
    res='' # 출력

    for x in a:
        if x.isalpha(): # 피연산자인지 아닌지 확인
            res+=x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x =='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    res+=stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res+=stack.pop()
                stack.pop()

    # 스택안에 남아있는 값들 pop            
    while stack:
        res += stack.pop()
    print(res)
    return

main()

"""
피연산자들은 바로 출력, 연산자들은 우선순위 고려해 스택에 저장
1. () 를 확인한다.
2.  * /인지를 확인하고 먼저 들어온, 같은 우선순위에 있는 * / 는 모두 결과문자열에 추가해준다.
3. 그리고 현재 문자를 다시 스택에 추가
4. +, - 인지 확인한다. + ,- 는 이들보다 낮은 우선순위의 연산자가 없으므로 자신보다 우선순위가 높은 것들을 모두 결과 문자열에 추가해준다.
5. ) 를 발견하면 ( 와 ) 사이에 있는 모든 연산자들을 결과문자열에 추가하고 (를 pop해준다.

출처: https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python [박지원]
"""