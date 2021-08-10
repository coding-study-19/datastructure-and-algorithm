# 2004 조합 0의 개수
import sys

#n!의 5 개수 세는 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

#n!의 2 개수 세는 함수
def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

def main():
    n, m = map(int, sys.stdin.readline().split())

    if m == 0:
        print(0)
    else:
        print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))

    return

main()

"""
nCr = n!/(n-r)!r! 을 이용하려 했지만, 입력 범위가 크므로 메모리 부족 현상이 발생한다.
끝이 0이 되려면 2x5 쌍이 1개 일 경우 뒤에 0이 한개 생기므로 2와5가 곱해진 개수를 세서 2와5의 지수 중 작은거를 선택하면 된다.
"""