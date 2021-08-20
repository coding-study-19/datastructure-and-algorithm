# 11052 카드 구매하기
import sys

def main():
    n = int(sys.stdin.readline())
    p = [0] + list(map(int, sys.stdin.readline().split()))
    note = [0] * (n + 1)
    note[1] = p[1]
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if note[i] < note[i - j] + p[j]:
                note[i] = note[i - j] + p[j]
    print(note[n])
    return

main()
