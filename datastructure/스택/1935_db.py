# 백준 | [203]자료구조1 | #1935 | 후위 표기식2 | 스택

import sys
input = sys.stdin.readline

N = int(input())
str = list(map(str, input().strip()))
num = [0] * N
for i in range(N):
    num[i] = int(input().strip())

st = []
for i in str:
    if i.isalpha():
        st.append(num[ord(i) - ord('A')])
    else:
        str2 = st.pop()
        str1 = st.pop()

        if i == '+':
            st.append(str1+str2)
        elif i == '-':
            st.append(str1-str2)
        elif i == '*':
            st.append(str1*str2)
        elif i == '/':
            st.append(str1/str2)

print('%.2f' %st[0])