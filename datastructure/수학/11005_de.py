# 11005 진법 변환 2

N, B = map(int, input().split())
result =""

while(1):
    mod = N % B
    N//=B
    code = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result +=code[mod]
    if N ==1:
        result += code[N]
        break
    elif N==0:
        break
print(result[::-1])
