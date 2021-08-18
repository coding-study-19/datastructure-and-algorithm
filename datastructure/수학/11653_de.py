# 11653 소인수분해
primes=[2,3,5,7]
N = int(input())

#보통 2 3 5 7로 나눠지기 때문에 대부분의 수를 여기서 걸러준다.
#에라토스테네스의 체 시간 너무 오래 걸림
for num in primes:
    if N%num==0:
        print(num)
        N//=num
        while(1):
            if N%num==0:
                print(num)
                N//=num
            else:
                break

# 위에서 걸러진 N의 약수를 11부터 N제곱근까지 반복문을 돌며 찾고(에라토스테네스 접근),
# 찾은 약수가 소수인지 검사한다.      
if N!=1:
    endN = int(N**0.5)+1
    for i in range(11,endN):
        if N==1: 
            break

        if N%i==0:
            check = True
            endI=int(i**0.5)+1
            for j in range(2,endI):
                if i%j==0:
                    check = False
                    break
            if check:
                print(i)
                N//=i
                while(1):
                    if N%i==0:
                        print(i)
                        N//=i
                    else:
                        break
    if N!=1:
        print(N)


#에라토스테네스 체
# arr= [True] * (N+1)
# end = int((N+1)**0.5)+1
# for i in range(11,end):
#     if arr[i]:
#         for j in range(i+i,N+1,i):
#             if arr[j]:
#                 arr[j] = False

# for i in range(11,N+1):
#     if arr[i]:
#         while(1): 
#             if (N%i)==0:
#                 print(i)
#                 N//=i
#             else:
#                 break 