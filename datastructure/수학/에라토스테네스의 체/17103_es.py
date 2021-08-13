# 17103 골드바흐 파티션
import sys

def eratos(n): # 에라토스테네스의 체
    sieve = [True] * (n+1) # 체
    sieve[0], sieve[1] = [False] * 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    sqrtN = int((n+1) ** 0.5)
    for i in range(2, sqrtN + 1):
        if sieve[i]:                        # i가 소수인 경우
            for j in range((i+i), (n+1), i):   # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # primeArr 생성
    # primeArr = list()
    # for i in range(2, (n+1)):
    #     if sieve[i]:
    #         primeArr.append(i)

    return sieve

def main():
    t = int(sys.stdin.readline())
    inputN = list()
    for _ in range(t):
        inputN.append(int(sys.stdin.readline()))

    sieve = eratos(max(inputN))
    for n in inputN:
        cnt = 0
        for i in range(n // 2 + 1):
            if sieve[i] and sieve[n-i]:
                cnt += 1
        print(cnt)

    return

main()
