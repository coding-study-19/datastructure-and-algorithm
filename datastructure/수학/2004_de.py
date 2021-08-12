# 2004 조합 0의 개수
# numList = list(map(int,sys.stdin.readline().split()))
# n = numList[0]
# m = numList[1]

n,m = map(int, input().split())
nm = n-m

def two_cnt(n):
    cnt =0
    while n!=0:
        n//=2
        cnt+=n
    return cnt
def five_cnt(n):
    cnt = 0
    while n!=0:
        n//=5
        cnt+=n
    return cnt

print(min(two_cnt(n) - two_cnt(m)-two_cnt(nm), five_cnt(n)-five_cnt(m)-five_cnt(nm)))