# 1158 요세푸스 문제
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    people = [_ for _ in range(1, n+1)]
    result = list()
    idx = 0
    while people:
        idx = (idx + k - 1) % len(people)
        result.append(people.pop(idx))
    print("<" + ", ".join(map(str, result)) + ">")
    return

main()
