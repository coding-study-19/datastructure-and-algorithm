# 11726 2xn 타일링
import sys

def main():
    note = [0, 1, 2]
    for i in range(3, 1001):
        note.append(note[i - 2] + note[i - 1])

    n = int(sys.stdin.readline())
    print(note[n] % 10007)
    return

main()
