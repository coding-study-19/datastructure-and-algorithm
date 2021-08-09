# 2609 최대공약수와 최소공배수
import sys

# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b = map(int, sys.stdin.readline().split())

    print(gcd(a, b))
    print(lcm(a, b))

    return

main()

"""
호제법 : 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘

2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),
a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다.
(최소공배수 x 최대 공약수) = gcd^2 * a * b [a, b은 서로수] => a * b
를 이용한 방법니다.

[출처] https://velog.io/@junyp1/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95
"""