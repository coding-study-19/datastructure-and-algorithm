# 백준 | [300]수학1 | #6588 | 골드바흐의 추측 | 에라토스테네스의 체

def isPrime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n**0.5)+1) :
        if n%i == 0:
            return False
    return True

n = int(input())
while (n!=0) :
    for k in range(3, n-2, 2) :
        if isPrime(k) :
            a = k
            b = n-a
            if isPrime(b) :
                Goldbach = True
                break
            else :
                Goldbach = False
        else :
            Goldbach = False

    if Goldbach :
        print(f'{n} = {a} + {b}')
    else :
        print("Goldbach's conjecture is wrong.")

    n = int(input())