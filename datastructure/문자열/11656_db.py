# 백준 | [203]자료구조1 | #11656 | 접미사 배열 | 문자열

S = input().rstrip('\n')
str = []

for i in range(len(S)):
    str.append(S[i:])

str.sort()
for i in str:
    print(i)