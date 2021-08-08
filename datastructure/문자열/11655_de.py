#11655 ROT13

import sys
# 파이썬 문장 끝이 개행이어야 입력이 되었다는 뜻이인가 end=""이 문제가 아니라 첫 문장 받고 개행이 없어서
# 계속 기다린거..? 그럼 지금까진 어케 됐지 이게
while(1):
    sentence = sys.stdin.readline().rstrip("\n")
    if not sentence:
        break

    for each in sentence:
        if each.isupper():
            if ord(each)<78:
                print(chr(ord(each)+13),end="")
            else:
                print(chr(65 + (ord(each) + 13)%91),end="")
        elif each.islower():
            if ord(each)<110:
                print(chr(ord(each)+13),end="")
            else:
                print(chr(97 + (ord(each) + 13)%123),end="")
        else:
            print(each,end="")


