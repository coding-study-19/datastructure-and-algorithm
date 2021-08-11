# 6588 골드바흐의 추측
import sys
import math

while(1):
    num = int(sys.stdin.readline())
    #EOF 조건
    if num==0:
        break
    # num에 대해 첫번째 피연산자가 소수인지 검사
    for operand1 in range(3, num, 2):
        isPrime =True
        #에라토스테네스의 접근
        for i in range(2,int(math.sqrt(operand1)+1)):
            if operand1 % i ==0:
                isPrime = False
                break
        #첫번째 피연산자가 소수일 경우 두번째 피연산자가 소수인지 검사
        if isPrime:
            operand2 = num - operand1
            #에라토스테네스의 접근
            for i in range(2, int(math.sqrt(operand2)+1)):
                if operand2 % i ==0:
                    isPrime = False
                    break
        #두 피연산자가 모두 소수일 경우 프린트
        if isPrime:
            print(f"{num} = {operand1} + {operand2}")
            break
