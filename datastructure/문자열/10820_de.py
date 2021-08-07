# 10820 문자열 분석
import sys
#EOF 처리!!!!
while True:
    sentence = sys.stdin.readline().rstrip("\n")
    if not sentence:
        break
    count=[0,0,0,0]
    for char in sentence:
        if char.islower():
            count[0]+=1
        elif char.isupper():
            count[1]+=1
        elif char.isnumeric():
            count[2]+=1
        elif char.isspace():
            count[3]+=1
    print(" ".join(list(map(str,count))))