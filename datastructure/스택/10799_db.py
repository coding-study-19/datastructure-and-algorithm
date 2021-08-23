# 백준 | [201]자료구조1 | #10799 | 쇠막대기 | 스택

import sys
input = sys.stdin.readline

S = list(input().strip())
result = 0
st = []

for i in range(len(S)):
    if S[i] == '(':
        st.append('(')
    else: #S[i] == ')'
        if S[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1

print(result)
