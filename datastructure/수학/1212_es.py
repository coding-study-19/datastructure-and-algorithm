# 1212 8진수 2진수
import sys

# 직접 작성 (시간 초과)
def octToDec(octN): # 8진수 -> 10진수
    decN = 0
    digit = len(octN)
    for i in range(digit):
        decN += int(octN[-1]) * (8**i)
        octN = octN[:-1]
    return decN

def decToBin(decN): # 10진수 -> 2진수
    binN = ""
    while decN != 0:
        binN += str(decN % 2)
        decN //= 2
    return binN[::-1]

def main1():
    octN = sys.stdin.readline().strip()
    decN = octToDec(octN)
    binN = decToBin(decN)
    print(binN)
    return

# 내장함수 사용
def main2():
    octN = int(sys.stdin.readline(), 8) # 8진수로 입력 받음
    binN = bin(octN)[2:] # 0b 제외
    print(binN)
    return

main2()
