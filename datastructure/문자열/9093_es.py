# 9093 단어 뒤집기
import sys

def flip_word(sentence):
    for word in sentence:
        print("".join(reversed(list(word))), end=" ")
    return

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        sentence = sys.stdin.readline().split()
        flip_word(sentence)
    return

main()