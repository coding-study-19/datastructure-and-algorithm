# 15988 1,2,3 더하기 3
import sys

def main():
    t = int(sys.stdin.readline())
    nArr = []
    for _ in range(t):
        nArr.append(int(sys.stdin.readline()))

    maxN = max(nArr)
    note = [1, 1, 2]
    for i in range(3, maxN+1):
        note.append(note[i-3] % 1000000009 + note[i-2] % 1000000009 + note[i-1] % 1000000009)

    for n in nArr:
        print(note[n] % 1000000009)
    return

main()
