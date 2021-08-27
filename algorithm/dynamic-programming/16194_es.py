# 16194 카드 구매하기 2
import sys

def main():
    n = int(sys.stdin.readline())
    p = [0] + list(map(int, sys.stdin.readline().split()))

    note = [float('inf')] * (n + 1)
    note[0] = 0

    for i in range(n + 1):
        for j in range(i + 1):
            note[i] = min(note[i], p[j] + note[i-j])

    print(note[n])
    return

main()
