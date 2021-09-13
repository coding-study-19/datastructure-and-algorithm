# 백준 | [301]수학1 (연습) | #9613 | GCD 합 | 수학

import sys
input = sys.stdin.readline

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(n):
    arr = list(map(int, input().split()))
    k = arr.pop(0)

    sum = 0
    for i in range(k):
        for j in range(k):
            if i < j :
                sum += gcd(arr[i], arr[j])
    print(sum)