# ✏️노트


## 파이썬 입력 받기 (sys.stdin.readline)

반복문으로 여러줄 입력 받는 상황에서 ```input()```을 사용할 경우 시간 초과가 발생할 수 있기 때문에 ```sys.stdin.readline()```을 사용해야 시간 초과가 발생하지 않는다.

```sys.stdin.readline()```은 개행문자를 포함하여 한 줄 단위로 입력 받는 함수이다.

#### 정수 입력 받기

- 한 개의 정수를 입력받을 때
    ```python
    import sys
    a = int(sys.stdin.readline())
    ```

- 정해진 개수의 정수를 한줄에 입력받을 때
    ```python
    import sys
    a,b,c = map(int, sys.stdin.readline().split())
    ```
    + ```map(func, list)```은 입력받은 자료형의 각 요소를 함수 func가 수행한 결과를 묶어서 돌려주는 함수이다.
    + ```str.split()```은 공백을 기준으로 문자열을 나눠주는 함수이다. 인자 값이 있을 경우에는 해당 값을 구분자로 문자열을 나눠준다.

- 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
    ```python
    import sys
    data = list(map(int, sys.stdin.readline().split()))
    ```

- 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
    ```python
    import sys
    data = []
    n = int(sys.stdin.readline())
    for _ in range(n):
        data.append(list(map(int,sys.stdin.readline().split())))
    ```

#### 문자, 문자열 입력 받기

- 임의의 개수의 문자/문자열을 공백을 구분자로 한줄에 입력받아 리스트에 저장할 때
    ```python
    import sys
    data = sys.stdin.readline().split()
    ```

- 개행문자를 제외하고 문자열을 입력받을 때
    ```python
    import sys
    data = sys.stdin.readline().strip()
    ```
    + ```str.strip()```은 문자열 str의 맨 앞과 맨 끝의 공백문자를 제거하는 함수이다.

- 임의의 개수의 문자를 공백 없이 한줄에 입력받아 리스트에 저장할 때
    ```python
    import sys
    data = list(sys.stdin.readline().strip())
    ```
    + ```list(str)```은 문자열 str의 문자 하나하나를 요소로 리스트에 저장한다.

- 문자열 n줄을 입력받아 리스트에 저장할 때
    ```python
    import sys
    n = int(sys.stdin.readline())
    data = [sys.stdin.readline().strip() for _ in range(n)]
    ```


## 자주 사용되는 함수

- ```"".join(list)```

    매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수



---
#### 출처
- [파이썬 입력 받기](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
- [점프 투 파이썬](https://wikidocs.net/book/1)
- [파이썬 join 함수](https://blockdmask.tistory.com/468)
