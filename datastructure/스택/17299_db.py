# 백준 | [201]자료구조1 | #17299 | 오등큰수 |

import sys
input = sys.stdin.readline
from collections import Counter

# 입력
N = int(input())
N_list = list(map(int, input().strip().split()))

# 수열 내 등장 횟수 세기
count_list = Counter(N_list)

# 오등큰수 판별
st = []
result = [-1] * N

for i in range(N):
    while st and count_list[N_list[st[-1]]] < count_list[N_list[i]]:
        result[st.pop()] = N_list[i]

print(*result)
