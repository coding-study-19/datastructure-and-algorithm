# 백준 | [203]자료구조1 | #11655 | ROT13 | 문자열

import sys
input = sys.stdin.readline

S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

answer = []
for i in S:
    if i.islower():
        index = (alpha.index(i) + 13) % 26
        answer.append(alpha[index])
    elif i.isupper():
        i = i.lower()
        index = (alpha.index(i) + 13) % 26
        answer.append(alpha[index].upper())
    else:
        answer.append(i)

for i in answer:
    print(i, end='')