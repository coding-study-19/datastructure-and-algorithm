# 2089 -2진수
import sys

def minBinary(n):
    if not n:
        return "0"

    result = ""
    while n:
        if n % (-2):
            result = "1" + result
            n = n // (-2) + 1
        else:
            result = "0" + result
            n //= (-2)

    return result

def main():
    n = int(sys.stdin.readline())
    print(minBinary(n))
    return

main()
