import sys

# for i in range (num) / for i in num -> 다르다 !!!!!! range 사용할때는 괄호로 묶어서!!!!
# l[::-1] 이런식으로 표현하면 거꾸로 반환. l이 문자열이어도, 리스트여도 가능. 
# ex) 리스트 / l= ['hello', 'my', 'name', 'is', 'chaewon'] -> l[::-1] = ['chaewon', 'is', 'name', 'my', 'hello'] 요소를 거꾸로
# ex) 문자열 / l = hello -> l[::-1] = olleh 

# num = int(sys.stdin.readline())
# for i in range (num):
#     tmp = sys.stdin.readline()
#     tmp_l = tmp.split()
#     output = list()
#     for a in tmp_l:
#         output.append(a[::-1])
#     print(" ".join(output))


# num = int(sys.stdin.readline())
# for i in range (num):
#     tmp = sys.stdin.readline().split()
#     for a in tmp:
#         print(a[::-1], end=' ')


# reversed 함수 사용. 얘는 이터레이터의 데이터를 반환해서 join으로 string으로 바꿔줘야함
# join은 리스트를 튜플로 만들어줄 수도 있다. 
num = int(sys.stdin.readline())
for i in range (num):
    tmp = sys.stdin.readline().split()
    for a in tmp:
        print("".join(reversed(a)), end=' ')

        
# 새롭게 알게 된것 -> join(), reversed()