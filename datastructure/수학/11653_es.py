# 11653 소인수분해
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
    primeArr = list()
    for i in range(2, (n+1)):
        if sieve[i]:
            primeArr.append(i)

    return primeArr

def prime_fact(n):
    if n == 1:
        return
    primeArr = eratos(n)
    idx = 0
    while n > 1:
        if n % primeArr[idx] == 0:
            print(primeArr[idx])
            n //= primeArr[idx]
        else:
            idx += 1

def main():
    n = int(sys.stdin.readline())
    prime_fact(n)
    return

main()
