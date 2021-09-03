# 백준 | [300]수학1 | #10430 | 나머지 | 수학

A,B,C = map(int,input().split())

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')