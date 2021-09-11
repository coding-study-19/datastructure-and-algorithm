# 백준 | [300]수학1 | #2004 | 조합 0의 개수 | 수학

def count(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, m = map(int, input().rstrip('\n').split( ))

five_count = count(n, 5) - count(m, 5) - count(n-m, 5)
two_count = count(n, 2) - count(m, 2) - count(n-m, 2)

answer = min(five_count, two_count)
print(answer)