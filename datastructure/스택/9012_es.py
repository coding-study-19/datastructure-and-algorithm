# 9012 괄호
import sys

# 올바른 괄호 문자열 (Valid PS, VPS)
def isVPS(ps):
    cnt = 0
    for p in ps:
        if p == '(':
            cnt += 1
        elif p == ')':
            cnt -= 1
            if cnt < 0:
                print("NO")
                return
    if cnt == 0:
        print("YES")
    else:
        print("NO")
    return

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        ps = sys.stdin.readline() # 괄호 문자열 (Parenthesis String, PS)
        isVPS(ps)
    return

main()