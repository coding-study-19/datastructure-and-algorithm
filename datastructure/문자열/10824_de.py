# 10824 네수

numbers = input().split()
print(int(numbers[0]+numbers[1])+int(numbers[2]+numbers[3]))
#파이썬에선 문자열도 시퀀스 객체이므로 시퀀스 객체의 공통적인 연산이 가능하다는 것을 항상 숙지하기
#문자열을 리스트처럼 다룰 수 있다는 것 인지!



#기존 코드
# import sys
# numbers = sys.stdin.readline().split()
# num1 = int("".join(numbers[:2]))
# num2 = int("".join(numbers[2:]))
# print(num1+num2)