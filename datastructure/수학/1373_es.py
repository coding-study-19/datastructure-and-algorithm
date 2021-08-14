# 1373 2진수 8진수
import sys

# 직접 작성 (시간 초과)
def binToDec(binN): # 2진수 -> 10진수
    decN = 0
    digit = len(binN)
    for i in range(digit):
        decN += int(binN[-1]) * (2**i)
        binN = binN[:-1]
    return decN

def decToOct(decN): # 10진수 -> 8진수
    octN = ""
    while decN != 0:
        octN += str(decN % 8)
        decN //= 8
    return octN[::-1]

def main():
    binN = sys.stdin.readline().strip()
    decN = binToDec(binN)
    octN = decToOct(decN)
    print(octN)
    return

# main()

# 내장함수 사용
print(oct(int(input(),2))[2:])
