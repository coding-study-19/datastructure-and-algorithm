import sys

T = int(sys.stdin.readline())

for i in range(T):
    word = sys.stdin.readline().split()
    for j in word:
        print("".join(reversed(j)), end=" ")
    print()