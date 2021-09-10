# 백준 | [203]자료구조1 | #10820 | 문자열 분석 | 문자열

import sys
input = sys.stdin.readline
output = sys.stdout.write

while True:
    str = input().rstrip('\n')
    lower, upper, num, blank = 0, 0, 0, 0

    if not str:
        break
    for i in str:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            blank += 1

    output("{} {} {} {}\n" .format(lower, upper, num, blank))
