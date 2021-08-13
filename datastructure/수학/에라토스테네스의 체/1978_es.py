# 1978 소수 찾기
import sys

def isPrime(n): # 노가다
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eratos(): # 에라토스테네스의 체
    sieve = [True] * 1001
    sieve[0], sieve[1] = [False] * 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    sqrtN = int(1001 ** 0.5)
    for i in range(2, sqrtN + 1):
        if sieve[i]:                        # i가 소수인 경우
            for j in range(i+i, 1001, i):   # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return sieve


def main():
    int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    # # 노가다
    # for n in arr:
    #     if isPrime(n):
    #         cnt += 1

    # 에라토스테네스의 체
    sieve = eratos()
    for n in arr:
        if sieve[n] == True:
            cnt += 1

    print(cnt)
    return

main()


"""
소수 : 1과 그 수 자신 이외의 자연수로는 나눌 수 없는 자연수

에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
1. 1은 제거
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
5. (반복)

[출처] https://wikidocs.net/21638
"""