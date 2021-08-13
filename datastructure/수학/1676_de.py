# 1676 팩토리얼 0의 개수

N = int(input())
#팩토리얼 구하기
result = 1
for i in range(1,N+1):
    result*=i

# 0 개수 구하기
result = str(result)
count = 0
for i in range(len(result)):
    if result[-i] =="0":
        count+=1
    elif count !=0:
        break
print(count)