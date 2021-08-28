# 백준 | [203]자료구조1 | #10809 | 알파벳 찾기 | 문자열

S = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(S.find(chr(x)), end=' ')