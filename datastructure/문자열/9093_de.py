#9093 단어 뒤집기 
import sys
T = int(sys.stdin.readline())

for i in range(T):
    sentence = sys.stdin.readline().split()
    for j in range(len(sentence)):
        for k in range(len(sentence[j])-1,-1,-1):
            print(sentence[j][k], end="")
        print(" " ,end="")
    print()

#"".join(reversed(list(리스트)))를 통해 간단히 구현 가능

#.join(리스트) , '구분자'.join(리스트)
# => join함수는 매개변수의 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로
#바꾸어 반환하는 함수. 앞의 구분자를 지정할 수 있다.

#reverse() , reversed(리스트)
#reverse() : 리스트를 역으로 만들어주는 함수. 메소드 자체의 반환 값이 없다
#reversed(리스트) : 리스트를 역으로 만들어주는 함수. 값을 반환한다.