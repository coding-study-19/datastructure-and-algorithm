#11655 ROT13

import sys

while(1):
    sentence = sys.stdin.readline()
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


