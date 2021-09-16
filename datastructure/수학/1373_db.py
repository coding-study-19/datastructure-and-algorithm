# 백준 | [301]수학1 (연습) | #1373 | 2진수 8진수 | 수학

two_num = list(map(int, input()))

answer = ''
sum, cnt = 0, 0

for i in two_num[::-1]:
    if cnt % 3 == 0:
        sum += i * 1
        cnt += 1
    elif cnt % 3 == 1:
        sum += int(i) * 2
        cnt += 1
    elif cnt % 3 == 2:
        sum += int(i) * 4
        answer += str(sum)
        sum, cnt = 0, 0

if sum >=0:
    answer += str(sum)
answer = int(answer[::-1])

print(answer)