# 1406 에디터
import sys

def editor_timeout():
    s = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    cursor = len(s)

    for _ in range(m):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'L':
            if cursor == 0:
                continue
            cursor -= 1
        elif cmd[0] == 'D':
            if cursor == len(s):
                continue
            cursor += 1
        elif cmd[0] == 'B':
            if cursor == 0:
                continue
            s = s[:cursor-1] + s[cursor:] # slice time complexity O(n)
            cursor -= 1
        elif cmd[0] == 'P':
            s = s[:cursor] + cmd[1] + s[cursor:] # slice time complexity O(n)
            cursor += 1

    print(s)
    return

# append, pop을 사용할 경우 time complexity O(1)로 해결 가능
def main():
    leftStack = list(sys.stdin.readline().strip())
    rightStack = list()
    m = int(sys.stdin.readline())

    for _ in range(m):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'L' and leftStack != []:
            rightStack.append(leftStack.pop())
        elif cmd[0] == 'D' and rightStack != []:
            leftStack.append(rightStack.pop())
        elif cmd[0] == 'B' and leftStack != []:
            leftStack.pop()
        elif cmd[0] == 'P':
            leftStack.append(cmd[1])

    rightStack.reverse()
    print("".join(leftStack + rightStack))
    return

main()
