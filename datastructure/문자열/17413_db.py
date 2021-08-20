# 백준 | [201]자료구조1 | #17413 | 단어 뒤집기 2 |

import sys
input = sys.stdin.readline

S = list(input().rstrip())
tag = False
word = ''
result = ''

for i in S:
    if tag == False:
        if i == '<':
            tag = True
            word += i
        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word = i + word

    elif tag == True:
        word += i
        if i == '>':
            tag = False
            result += word
            word = ''

print(result + word)