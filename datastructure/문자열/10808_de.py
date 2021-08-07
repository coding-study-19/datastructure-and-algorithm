# 10808 알파벳 개수
s = input()
count = [0]*26
# 파이썬에서 아스키 코드 이용 ord, chr
for each in s:
    count[ord(each)-97]+=1
print(" ".join(list(map(str, count))))
