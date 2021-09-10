# 백준 | [300]수학1 | #10872 | 팩토리얼 | 수학

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))