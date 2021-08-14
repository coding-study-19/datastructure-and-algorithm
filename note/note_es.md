# ✏️노트


## 1. 파이썬 입력 받기 (sys.stdin.readline)

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

#### readline()과 input()의 EOF 입력시 차이점
- ```input()```은 EOFError를 발생시킨다.

- ```sys.stdin.readline()```은 빈 문자열을 반환한다.
    ```python
    import sys

    sentence = sys.stdin.readline()
    if not sentence:
        break
    ```


## 2. 파이썬 자료형 별 주요 연산자의 시간 복잡도 (Big-O)

<img src="https://user-images.githubusercontent.com/55284181/127728331-099ce209-463a-4461-ac4c-9063a210ff30.png" width="500">

#### list
|Operation|Example|Big-O|Notes|
|:---|:---|:---|:---|
|Index	        |l[i]	            |O(1)	    ||
|Store	        |l[i] = 0	        |O(1)	    ||
|Length	        |len(l)	            |O(1)	    ||
|Append	        |l.append(5)	    |O(1)	    ||
|Pop	        |l.pop()	        |O(1)	    |l.pop(-1) 과 동일|
|Clear	        |l.clear()	        |O(1)	    |l = [] 과 유사|
|Slice	        |l[a:b]	            |O(b-a)	    |슬라이싱되는 요소의 개수에 비례; l[:] : O(len(l)-0)=O(N)|
|Extend	        |l.extend(l2)	    |O(len(l2))	|확장 길이에 따라|
|Construction	|list(…)	        |O(len(…))	|요소 길이에 따라|
|check ==, !=	|l1 == l2	        |O(N)	    |전체 리스트 비교|
|Insert	        |l.insert(i, v)     |O(N)	    |i 위치에 v를 추가|
|Pop	        |l.pop(i)	        |O(N)	    |리스트 재배치 필요; l.pop(0) : O(N)|
|Delete         |del l[i]	        |O(N)	    |리스트 재배치 필요; 최악의 경우 O(N)|
|Remove	        |l.remove(x))	    |O(N)	    |리스트 재배치 필요|
|Copy	        |l.copy()	        |O(N)	    |l[:]과 동일 : O(N)|
|Containment	|x in / not in l	|O(N)	    |선형 검색|
|Extreme value	|min(l) / max(l)	|O(N)	    |선형 검색|
|Reverse	    |l.reverse()	    |O(N)	    ||
|Iteration	    |for v in l:	    |O(N)	    |return/break이 없는 최악의 경우 O(N)|
|Sort	        |l.sort()	        |O(N Log N)	||
|Multiply	    |k * l	            |O(k N)	    |3*[1,2,3] : O(N**2)|

- slice, pop, del, remove 비교
    
        del이 가장 빠르고 pop()과 remove()는 비슷한 수행시간을 가지며 슬라이싱이 가장 느리다.

    + **slice** : 원본 리스트는 유지하고, 추출하고자 하는 내용을 새롭게 메모리에 할당한다.
    + **pop** : 지우고자 하는 리스트의 인덱스를 인자로 받는다. 원본 리스트 변형 후 떼어낸 원소를 리턴한다. 제거된 값 이후를 전부 한칸씩 당겨줘야 한다.
    + **del** : pop과 마찬가지로 지우고자 하는 리스트의 인덱스를 인자로 받는다. 제거된 값 이후를 전부 한칸씩 당겨줘야 한다.
    + **remove** : 지우고자 하는 값을 인자로 받는다. 만약 지우고자 하는 값이 리스트 내에 2개 이상일 경우 순서상 가장 앞에 있는 값을 지운다. 해당 값을 삭제한 후, 제거된 값 이후를 전부 한칸씩 당겨줘야 한다.
    + 원본 리스트의 요소 개수가 적을 경우, 슬라이싱이 pop()보다 빠를 수 있다.

#### Dict
|Operation|Example|Big-O|Notes|
|:---|:---|:---|:---|
|Index	        |d[k]	        |O(1)       ||
|Store	        |d[k] = v	    |O(1)       ||
|Length	        |len(d)	        |O(1)       ||
|Delete	        |del d[k]	    |O(1)       ||
|get/setdefault	|d.method	    |O(1)       ||
|Pop	        |d.pop(k)	    |O(1)       ||
|Pop item	    |d.popitem()	|O(1)       ||
|Clear	        |d.clear()	    |O(1)	    |s = {} or = dict() 유사|
|View	        |d.keys()	    |O(1)	    |d.values() 동일|
|Construction	|dict(…)	    |O(len(…))  ||
|Iteration	    |for k in d:	|O(N)       ||


## 3. 자주 사용되는 함수

- ```"".join(list)``` : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수


## 4. 입출력 관련 issue
> 실습 환경 : Ubuntu20.04 terminal

### 4-1. issue
아래와 같이 코드 작성 시 (의미 없는 코드) 문자열이 화면에 출력되지 않는 문제가 발생하였다.

```python
import sys

s = sys.stdin.readline().strip() # 문자열에서 개행문자 제거
for i in s:
    print(s, end="")

while (1): # 무한루프
    continue
```

```python
s = "abcde".strip() # 문자열에서 개행문자 제거
for i in s:
    print(s, end="")

while (1): # 무한루프
    continue
```

### 4-2. 스트림과 버퍼 (C/C++)
- 스트림(stream)

    <img src="https://user-images.githubusercontent.com/55284181/128626958-7bf78e70-441a-4f52-8c09-9a7d08286e7f.png" width="500" title="stream">

    C, C++ 프로그램은 파일이나 콘솔의 입출력을 직접 다루지 않고, 스트림(stream)이라는 흐름을 통해 다룬다.
    스트림(stream)이란 **실제의 입력이나 출력이 표현된 데이터의 이상화된 흐름**을 의미한다.
    즉, 스트림은 운영체제에 의해 생성되는 가상의 연결 고리를 의미하며, 중간 매개자 역할을 한다.

    <img src="https://user-images.githubusercontent.com/55284181/128626959-056abbff-1795-462f-8b41-5dfb82a65a25.png" width="500" title="stream io">

    콘솔 장치에 대한 스트림은 프로그램 실행 시 자동으로 생성되며, 프로그램 종료 시 자동으로 소멸한다.

- 버퍼(buffer)

    <img src="https://user-images.githubusercontent.com/55284181/128626957-d068eace-0b5f-4259-a921-61188d44168d.png" width="500" title="buffer">

    C++ 프로그램의 경우 스트림은 내부에 버퍼(buffer)라는 **임시 메모리 공간**을 가지고 있다.
    또한, C언어의 표준 입출력 함수를 사용할 때 역시 버퍼(buffer)를 사용하게 된다.
    이러한 버퍼를 이용하면 입력과 출력을 좀 더 효율적으로 처리할 수 있게 된다.

- 입출력 버퍼

    C 언어의 입출력 함수들은 내부적으로 입출력 버퍼를 사용하여 데이터를 처리한다.

    표준 입력(키보드)은 입력되는 문자를 입력 버퍼에 저장했다가 엔터 키(\n)가 입력되면 지정된 변수(배열, 할당한 메모리)로 옮긴다(버퍼가 비워짐).
    마찬가지로 표준 출력(화면)은 출력 버퍼에 문자가 저장되었다가 특정 조건에 의해 버퍼가 비워지면 화면에 출력된다(입출력 버퍼가 비워지는 시점은 운영체제나 설정에 따라 달라짐).
    이처럼 입출력 버퍼에 데이터를 저장하는 행동을 **버퍼링(buffering)** 이라고 부른다.

- 버퍼링 방식(Buffering modes) - C Standard I/O

    - line buffered : newline 을 만나면 출력한다. 보통 키보드 입력에서 사용된다.
    - full buffered : 버퍼가 차면 출력한다. 보통 파일 입출력에서 사용된다.
    - unbuffered : 버퍼링을 하지 않고 바로 출력한다. (1 byte)

    명령이 실행되면 자동으로 stdin, stdout, stderr 세 개의 stream 이 생성되는데 버퍼와 관련해서 각각 다음과 같은 특징이 있다.

    - stdin : 터미널에서 입력을 받으면 line buffered or unbuffered 이고 그외는 full buffered 이다.
    - stdout : 터미널에 연결되어 있으면 line buffered 이고 그외는 full buffered 이다.
    - stderr : 항상 unbuffered 입니다. 그러므로 stderr 로 메시지를 출력하면 바로 표시가 된다.

    이러한 입력 작업뿐만 아니라 ```printf()``` 함수 등을 통해 모니터에 데이터를 출력할 때도 버퍼를 사용한다.
    출력하고자 하는 데이터는 일단 출력 버퍼에 저장되었다가 출력 스트림을 통해 모니터로 전송된다.



### 4-3. Python ```print()``` 함수
- 공식 문서

    ```python
    >>> help(print)
    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    ```

- flush

    문서에서 flush에 대한 해석을 직역하면 **"스트림을 강제로 플러시할지에 대한 여부"** 를 의미한다.

    키보드와 화면 사이에는 '버퍼(buffer)' 개념 또는 장치가 있어서 버퍼에서 내용을 출력 전에 잠시 보관하게 된다. flush는 키보드에서 입력되어 버퍼에 저장된 내용을 출력방향(화면)으로 바로 밀어넣는다는 의미이다.
    
    버퍼에 값이 들어올 때마다 flush를 해주는 것은 성능 면에서 비용이 크기 때문에, 기본 설정값은 ```flush = False``` 이다.
    이를 ```flush = True```로 설정하면 print() 함수가 실행될 때마다 스트림이 강제로 flush(clear)되어 출력방향(화면)에 바로 출력된다.

    ```python
    import time

    for i in range(10):
        print(i, end = ' ')
        time.sleep(1) 
    ```

    위와 같이 코드를 작성할 경우 ```flush = False```인 상태에서도 조금 늦게 flush가 되어 화면에 출력되는 것을 볼 수 있다.
    파이썬의 end parameter로 설정된 ```\n```의 경우 바로 내용이 flush되지만, ' '의 경우 output이 buffered 상태여서 9초가 지난 후 10초에 모든 숫자가 동시에 출력되는 것이다.
    이는 실습 환경에 따라 결과가 달라질 수 있다.

- 파이썬 ```print()``` 함수 출력 조건 (실제와 다를 수 있음)

    - 출력 버퍼가 가득 찼을 때
    - 개행문자 ```\n```을 만났을 때
    - 프로그램이 종료됐을 때
    - 출력 버퍼가 buffered 상태에서 9초가 지난 후

- 임의로 생성하는 상수, 변수의 경우 파이썬이 알아서 개행문자를 붙여주는 것으로 추정된다.

    아래 코드처럼 ```strip()``` 함수로 개행문자를 없애주지 않으면 출력이 정상적으로 이루어진다.
    ```python
    s = "abcde"
    for i in s:
        print(s, end="")

    while (1): # 무한루프
        continue
    ```


## 5. 수학

### 5-1. 유클리드 호제법

#### 최대공약수
a, b의 공통된 약수 중, **가장 큰 약수**. 이때 최대공약수가 1이라면 a, b는 서로소(coprime)라고 한다. 시간복잡도는 ```O(n)``` 이다.

```python
def gcd(a, b):
    GCD = 1  # 어차피 공약수에 1은 무조건 들어가므로...
    n = 2
    while n <= min(a,b):
        if (a % n == 0) and (b % n == 0):
            GCD = n
        n += 1
    return GCD
```

#### 유클리드 호제법으로 최대공약수 구하기
a,b의 최대공약수는 b와 a%b의 최대공약수와 같다. 시간복잡도는 ```O(log n)``` 이다.

```python
def gcd(a, b):
    if b == 0:
        return a
    else :
        return gcd(b, a%b)
```

### 5-2. 에라토스테네스의 체
범위에서 합성수를 지우는 방식으로 소수를 찾는 방법.
여기서 소수란, 1과 그 수 자신 이외의 자연수로는 나눌 수 없는 자연수이다.

1. 1은 제거
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
5. (반복)

```python
def eratos(n): # 에라토스테네스의 체
    sieve = [True] * (n+1) # 체
    sieve[0], sieve[1] = [False] * 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    sqrtN = int((n+1) ** 0.5)
    for i in range(2, sqrtN + 1):
        if sieve[i]:                        # i가 소수인 경우
            for j in range((i+i), (n+1), i):   # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # primeArr 생성
    primeArr = list()
    for i in range(2, (n+1)):
        if sieve[i]:
            primeArr.append(i)

    return primeArr
```


### 5-3. 진법 변환

#### X진수 -> 10진수
- 내장함수 ```int()``` 사용
    ```python
    int(string, base)

    print(int('111', 2)) # 7 출력
    ```

- 코드 직접 작성
    ```python
    def XToDec(X, n): # X진수 -> 10진수
        res = 0
        digit = len(n)
        for i in range(digit):
            res += int(n[-1]) * (X**i)
            n = n[:-1]
        return res
    ```

#### 10진수 -> X진수
- 내장함수 ```bin()```, ```oct()```, ```hex()``` 사용
    ```python
    print(bin(10)) # 2진수 - 0b1010 출력
    print(oct(10)) # 8진수 - 0o12 출력
    print(hex(10)) # 16진수 - 0xa 출력
    ```

- 코드 직접 작성
    ```python
    def DecToX(X, n): # 10진수 -> X진수
        res = ""
        while n != 0:
            res += str(n % X)
            n //= X
        return res[::-1]
    ```




---
### reference
- [마크다운 작성법](https://gist.github.com/ihoneymon/652be052a0727ad59601)
- [파이썬 입력 받기](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
- [점프 투 파이썬](https://wikidocs.net/book/1)
- [입출력에서 readline()과 input()의 EOF 입력시 차이점](https://joewithtech.tistory.com/26)
- [파이썬 자료형 별 주요 연산자의 시간 복잡도 (Big-O)](https://wayhome25.github.io/python/2017/06/14/time-complexity/)
- [알고리즘의 시간복잡도](https://debugdaldal.tistory.com/158)
- [slice, pop, del 성능 비교](https://brownbears.tistory.com/452)
- [파이썬 join 함수](https://blockdmask.tistory.com/468)
- [print() 함수의 새로운 면모(sep, end, file, flush)](https://velog.io/@janeljs/python-print-sep-end-file-flush)
- [python print advanced](https://gist.github.com/shoark7/fa0a66bfc37d63890603a276f974f0b6)
- [C++ 스트림과 버퍼](https://tcpschool.com/cpp/cpp_io_streamBuffer)
- [C언어 콘솔 입출력](http://tcpschool.com/c/c_io_console)
- [C언어 기본적인 입출력](http://tcpschool.com/c/c_string_io)
- [C언어 코딩도장 입출력 버퍼 활용하기](https://dojang.io/mod/page/view.php?id=763)
- [Buffering](https://mug896.github.io/bash-shell/buffering.html)
- [수학 : 유클리드 호제법, 에라토스테네스의 체](https://infinitt.tistory.com/232)
- [에라토스테네스의 체 wiki](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
- [1373번 파이썬(python) - 2진수 8진수](https://oort-cloud.tistory.com/entry/%EB%B0%B1%EC%A4%80-1373%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-2%EC%A7%84%EC%88%98-8%EC%A7%84%EC%88%98?category=881353)
