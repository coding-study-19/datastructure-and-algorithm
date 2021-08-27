# 백준 | [203]자료구조1 | #10808 | 알파벳 개수 | 문자열

result = [0] * 26

for i in input():
    result[ord(i) - ord('a')] += 1

print(*result)