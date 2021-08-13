# 1373 2진수 8진수

print(oct(int(input(),2))[2:])


# 기존 코드
# import math
# bin =input()
# bin = "".join(reversed(bin))

# addZero =  len(bin) % 3
# if addZero!=0:
#     bin +="0"*(3-addZero)

# cnt = 0
# sum = 0
# oct = ""
# for bit in bin:
#     if bit == "1":
#         sum+= int(math.pow(2,cnt))
#     cnt +=1
#     if cnt == 3:
#         oct+=str(sum)
#         sum=0
#         cnt=0
# print("".join(reversed(oct)))

