# 백준 | [300]수학1 | #1934 | 최소공배수 | 수학

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

T = int(input())
for i in range(T):
    a, b = map(int, input().rstrip('\n').split())
    print(lcm(a, b))
