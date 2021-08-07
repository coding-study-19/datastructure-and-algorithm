# 10809 알파벳 찾기
s=input()
location = [-1] * 26

for i in range(len(s)):
    if location[ord(s[i])-97]== -1:
        location[ord(s[i])-97] = i
print(" ".join(list(map(str,location))))