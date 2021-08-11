# 9613 GCD 합
import sys

def gcd(a, b):
    if b==0:
        return a
    else :
        return gcd(b,a%b)

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        arr = list(map(int, sys.stdin.readline().split()))

        sum = 0
        n = arr.pop(0)
        for i in range(n):
            for j in range(i+1, n):
                sum += gcd(arr[i], arr[j])

        print(sum)
    return

main()
