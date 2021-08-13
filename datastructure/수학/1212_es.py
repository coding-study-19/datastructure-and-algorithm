# 1212 8진수 2진수
import sys

def main():
    octN = int(sys.stdin.readline(), 8) # 8진수로 입력 받음
    binN = bin(octN)[2:] # 0b 제외
    print(binN)
    return

main()
