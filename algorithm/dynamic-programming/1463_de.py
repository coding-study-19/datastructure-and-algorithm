# 1463 1로 만들기

from collections import deque
N = int(input())
arr=deque()
arr.append(N)
count = 0

def calc(n):
    # 2또는 3으로 나누어 떨어지는 경우
    if n%3==0 and n%2==0:
        arr.append(n//3)
        arr.append(n//2)
        arr.append(n-1)
        return arr

    # 3으로만 나누어 떨어지는 경우
    elif n%3==0:
        arr.append(n//3)
        arr.append(n-1)
        return arr

    #  2로만 나누어 떨어지는 경우
    elif n%2==0:
        arr.append(n//2)
        arr.append(n-1)
        return arr

    #이외의 경우
    else:
        arr.append(n-1)
        return arr

while 1:
    if min(arr) == 1:
        break

    tmp = arr.copy()
    for num in tmp:
        calc(num)
        arr.popleft()

    count+=1
print(count)
#------------------------------


# def calc(n):
#     if n%3==0 and n%2==0:
#         return [n//3,n//2,n-1]

#     elif n%3==0:
#         return [n//3,n-1]

#     elif n%2==0:
#         return [n//2,n-1]

#     else:
#         return [n-1]

# arr = calc(N)
# tmp = arr.copy()
# count = 0

# while 1:
#     if min(arr) == 1:
#         break

#     for num in tmp:
#         calc(num)
#         arr.popleft()
#     count+=1

# print(count)


# 재귀는 재귀 횟수의 한계 때문에 실패
# def calc(n):
#     if arr[n]:
#         return arr[n]

#     if n==1:
#         return 0

#     # 2또는 3으로 나누어 떨어지는 경우
#     elif n%3==0 and n%2==0:
#         arr[n] = min(calc(n//3),calc(n//2),calc(n-1)) + 1
#         return arr[n]

#     # 3으로만 나누어 떨어지는 경우
#     elif n%3==0:
#         arr[n] = min(calc(n//3),calc(n-1)) +1
#         return arr[n]

#     #  2로만 나누어 떨어지는 경우
#     elif n%2==0:
#         arr[n] = min(calc(n//2),calc(n-1)) + 1
#         return arr[n]

#     #이외의 경우
#     else:
#         arr[n] = calc(n-1)+1
#         return arr[n]


