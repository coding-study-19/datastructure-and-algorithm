# 9095 1,2,3 더하기
import sys

def main():
    t = int(sys.stdin.readline())
    nArr = []
    for _ in range(t):
        nArr.append(int(sys.stdin.readline()))

    maxN = max(nArr)
    note = [1, 2, 4]
    for i in range(3, maxN+1):
        note.append(note[i-3] + note[i-2] + note[i-1])

    for n in nArr:
        print(note[n-1])
    return

main()
