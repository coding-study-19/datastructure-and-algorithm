# 백준 | [301]수학1 (연습) | #2089 | -2진수 | 수학

N = int(input())

if not N:
    print('0')
    exit()

res = ''
while N:
    if N % (-2):
        res = '1' + res
        N = N//-2 + 1
    else:
        res = '0' + res
        N //= -2

print(res)