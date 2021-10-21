<정리>
* [deque](https://appia.tistory.com/203)
* [인덱스 위치](https://ooyoung.tistory.com/78)
* [슬라이스](https://nirsa.tistory.com/41)
* [값 삭제](https://ponyozzang.tistory.com/587)
* [filter] (https://blockdmask.tistory.com/532)
* [filter](https://www.daleseo.com/python-filter/)
* [slice와reverse로 스택의 특정 구간 수정 가능](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/datastructure/%EB%AC%B8%EC%9E%90%EC%97%B4/17413_de.py)
* [mutable imutable](https://dpdpwl.tistory.com/82)
* [파이썬스러운 코드](https://velog.io/@hamdoe/python-cleancode-2.-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%8A%A4%EB%9F%AC%EC%9A%B4-%EC%BD%94%EB%93%9C)
# ✏️노트
---
## 📊파이썬 함수

### 1. join( )
```join함수```는 매개변수로 들어온 ```반복 가능한(iterable)```문자열 객체에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환한다.
* "구분자".join(리스트)
  
  * 리스트 요소와 요소 사이에 '구분자'를 넣어 하나의 문자열로 합쳐 반환할 수 있다.
    ```python
        a = ['a', 'b', 'c', 'd', '1', '2', '3']

        res1 = "".join(a)
        # abcd123
        res2 = ",".join(a)
        # a,b,c,d,1,2,3
        res3 = " ".join(a)
        # a b c d 1 2 3
     ```

### 2. map( )
```map```은 ```반복 가능한(iterable)객체```의요소를 지정된 함수로 처리해주는 함수다. map은 원본 객체를 변경하지 않고 새 객체를 생성한다. 보통 list나 tuple을 대상으로 주로 사용한다.
* map(변환 함수, iterable객체)
  
  * 두번째 인자로 넘어온 객체의 모든 요소에 변환 함수를 적용하여 저장한다.
    ```python
        a = [1.2, 2.5, 3.7, 4.6]
        # a 리스트의 요소를 int로 변환해 list로 만듦
        a = list(map(int,a))
        # a : [1,2,3,4]

        b = list(map(str, range(5)))
        # b : ['0','1','2','3','4']

        def squared(num):
            return num*num
        c = list(map(squared, range(5)))
        # c : [0,1,4,9,16]
    ```
#### map 활용

* 정해진 개수의 정수를 한줄에 입력 받을 때
    ```python
        import sys
        a,b,c = map(int, sys.stdin.readline().split())
    ```
* 정수 리스트를 join함수에 적용하고 싶을 때
    ```python
        a = [1,2,3,4,5]
        a = ",".join(list(map(str,a)))
        # a : "1,2,3,4,5"
    ```
### 3. isupeer( ), islower( ), isspace( ), isnumeric( )..
* 말 그대로 해석하면 된다. 대문자인지, 소문자인지, 공백인지, 숫자인지 등등..

  
    ```python 
        word = Ab 1
        word[0].isupper() #True
        word[1].islower() #True
        word[2].isspace() #True
        word[3].isnumeric() #True
    ```
* 관련 문제 : [백준 17413번](https://github.com/coding-study-19/datastructure)

### 4. ord( ), chr( )
```아스키코드 65 ~ 90```은 ```알파벳 대문자 A~Z```를, ```아스키코드 97~ 122```는 ```알파벳 소문자 a~z```를 의미한다.
* ord( ) 
  * 문자를 아스키코드로 변환하는 함수
* chr( )
  * 아스키코드를 문자로 변환하는 함수
    ```python 
        ord("A") #65
        ord("a") #97
        chr(65) #A
        chr(97) #a
    ```
* 관련 문제 : [백준 10808번](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/datastructure/%EB%AC%B8%EC%9E%90%EC%97%B4/10808_de.py)

### 5. 파이썬 진법 변환 함수

#### 1) n진수 -> 10진수
* int(string base) 함수<br>
    * base에 원하는 진법을 넣으면 string을 해당 진법의 수로 인식해 10진수로 변환해준다.
    ```python
        print(int('111',2)) #7
        print(int('222',3)) #26
        print(int('333',4)) #63
        print(int('444',5)) #124
        print(int('555',6)) #215
        print(int('FFF',16) #4095
    ```
#### 2) 10진수 -> 2,8,16진수
* 2,8,16 진수는 각각 bin( ), oct( ), hex( ) 함수를 지원한다.
* 앞의 진수 식별 문자를 없애고 출력하고 싶다면 슬라이싱을 이용하면 된다.

    ```python
        print(bin(10)) # 0b1010
        print(oct(10)) # 0o12
        print(hex(10)) # 0xa

        print(bin(10)[2:]) #1010
    ```
* 관련 문제 : [백준 1373번](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/datastructure/%EC%88%98%ED%95%99/1373_de.py)

### 6. slice
#### 6-1. extended slice
  arr[ : : ], arr[ 1 : 2 : 3 ], arr[ : : -1 ] 등으로 배열의 index에 접근하는 방법이다.
* ``arr[ A : B : C ]``
  * index A부터 index B-1까지 C의 간격으로 배열을 만든다.
  * ``A == None``일 경우 : 처음 index부터
  * ``B == None``일 경우 : 할 수 있는 데까지( C가 양수라면 마지막 index까지, C가 음수라면 처음 index까지)
  * ``C == None``일 경우 : 한칸 간격으로
    
    ```python
        arr = [i for i in range(10)] # [0,1,2,3,4,5,6,7,8,9]

        arr[::2] #[0,2,4,6,8]
        arr[1::2] #[1,3,5,7,9]
        arr[::-1] #[9,8,7,6,5,4,3,2,1,0] 역순
        <reverse를 사용할 수 없을 경우 이런식으로 역순을 구현할 수 있다.>
        arr[::-2] #[9,7,5,3,1]
        arr[3::-1] #[3,2,1,0]
        arr[1:6:2] #[1,3,5]
    ```
  * 관련 문제 :[백준 11005번](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/datastructure/%EC%88%98%ED%95%99/11005_de.py)


---
## 📌파이썬 개념
파이썬에서 중요한 개념 중에 하나가 "반복 가능한(iterable)"이다.
 어떤 메서드를 쓸 수 있냐, 없냐 는 해당 객체가 ```반복 가능한지```, ```시퀀스```인지에 따라 나뉜다. 공통 속성을 갖고 있다면 해당 기능을 쓸 수 있다.

시퀀스 객체야? 그러면 in을 쓸 수 있겠네?
반복 가능한 객체야? 그러면 for를 쓸 수 있겠네?

이렇게 생각할 수 있다. 따라서 문자열 따로, 리스트 따로, 튜플 따로 학습하는 것이 아니라 파이썬 표준에서 제시하는 기본 개념인 반복 가능한과 시퀀스를 이해하는 것이 중요하다.

![사진](https://dojang.io/pluginfile.php/13952/mod_page/content/3/039002.png)
### 1. 시퀀스 자료형(sequence)

파이썬에서는 ```리스트```, ```튜플```,``` range```, ```문자열```처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types)이라고 부른다.

#### 시퀀스 자료형의 공통 기능   

시퀀스 자료형의 가장 큰 특징은 공통된 동작과 기능을 제공한다는 점이다. 따라서 시퀀스 자료형의 기본적인 사용 방법을 익혀 두면 나중에 어떠한 시퀀스 자료형을 접하게 되더라도 큰 어려움 없이 바로 사용할 수 있다.

* 특정 값이 있는지 확인
  * 값 in 시퀀스 객체
  * 값 not in 시퀀스 객체
    ```python
        a = [1,2,3,4,5]
        1 in a # True
        1 not in a # False

        1 in (1,2,3,4,5) # True
        1 in range(5) # True
        'P' in 'Hello world' # False
    ```
  
* 시퀀스 객체 연결
  * 시퀀스 객체 + 시퀀스 객체
    ```python
        a = [0, 10, 20, 30] 
        b = [9, 8, 7, 6]
        a + b
        [0, 10, 20, 30, 9, 8, 7, 6]

        "Hello" + "world" # "Hello world"
    ```
  * ```range```는 + 사용 못해서 ```range```를 ```리스트``` 또는 ```튜플```로 변환해서 합친다   
    ```python
        list(range(5)) + list(range(5,10))
        # [0,1,2,3,4,5,6,7,8,9]
        tuple(range(5)) + tuple(range(5,10))
        # (0,1,2,3,4,5,6,7,8,9)
    ```
* 시퀀스 객체 반복
  * 시퀀스 객체 * 정수
    ```python
        [1,2,3,4,5] * 2
        # [1,2,3,4,5,1,2,3,4,5]

        "hello " * 3
        # "hello hello hello "
    ```
  * ```range```는 * 사용 못해서 ```range```를 ```리스트``` 또는 ```튜플```로 변환해서 반복한다.
    ```python
        list(range(5)) * 2
        # [0,1,2,3,4,0,1,2,3,4]
    ``` 
* 시퀀스 객체 요소 개수
    * len(시퀀스 객체)
    ```python
        a = [1,2,3,4]
        len(a) # 4
        len(range(5)) # 5
        len("hello") # 5
    ```
* 시퀀스 객체 인덱스
    * 시퀀스 객체[인덱스]
    ```python
        a = [1,2,3,4]
        a[1] # 2
        r = range(5)
        r[2] # 2
        word = "hello"
        word[-3] # l
    ```
### 2. 반복 가능한 객체(iterable))

*  반복 가능한 객체는 말 그대로 반복할 수 있는 객체인데 우리가 흔히 사용하는 ```문자열```, ```리스트```, ```딕셔너리```, ```세트```가 이에 해당한다. 즉, 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체를 의미한다.
  
* ```이터레이터(iterator)```는 값을 차례대로 꺼낼 수 있는 객체(object)다. 

  * [ 예시 ] ```for i in range(100)```는 0부터 99까지 연속된 숫자를 만들어낸다고 하는데, 사실은 숫자를 모두 만들어 내는 것이 아니라 0부터 99까지 값을 차례대로 꺼낼 수 있는 ```이터레이터```를 하나만 만들어내는 것이다. 이후 반복할 때마다 ```이터레이터```에서 숫자를 하나씩 꺼낸다. 만약 연속된 숫자를 미리 만들면 숫자가 많아질 때는 메모리를 많이 사용하게 되므로 성능이 저하되는데,파이썬에서는 ```이터레이터```만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용해 메모리 낭비를 줄인다.
*  iterable 확인
   * ``` dir(객체)```를 통해 객체에 ```__iter__``` 메서드가 있는지 확인한다.
* ```이터레이터(iterator)``` 호출
    ```python
        it = [1,2,3,4].__iter__()
        it.__next__() # 1
        it.__next__() # 2
        ...
        it2 = "hello world".__iter__()
        it2.__next__() # h
        it2.__next__() # e
        ...
        it2 = {'a':1,'b':2}.__iter__()
        it3.__next__() # a
        it3.__next__() # b
    ```
### 3. 파이썬의 변수
*  파이썬에서 데이터, 함수, 클래스, 모듈, 패키지 등은 모두 객체(object)로 취급한다. 대입연산자를 통해 복사되는 겻은 값이 아니라 참조하는 곳이다. 즉 변수는 객체를 참조하는 객체에 연결된 이름에 불과하다는 것.
* 그래서 C언어처럼 함수 내부에 선언한 지역 변수가 함수가 실행될 때 생성되고 종료될 때 소멸한다는 개념이 없다.
    ```python
        #값이 참조됨
        n = 17
        id(17) # 5678 
        id(n) # 5678
        
        #함수의 영향을 받지 않는 지역변수
        n=1
        def func():
            x=1
            id(x) #1234
        id(1) #1234
        id(n) #1234
    ```
#### 3-1. 얕은 복사, 깊은 복사
위에서 언급했다시피 파이썬에서 변수는 객체와 연결된 이름에 불과하다. 따라서 값의 복사와 값의 참조에서 문제가 생길 수 있다. 
* ``.copy( )``
  *  ``copy( )``는 ``얕은 복사``로 리스트 안의 모든 원소가 참조하는 곳까지 복사된다. 즉 리스트를 복사한 후 원소값을 변경하면 복사된 원소값도 변경될 수 있다는 것이다.
  
        ```python
            import copy

            x = [[1,2],[3,4]]
            y = x.copy()
            x[0][1] = 9
            # x : [[1,9],[3,4]]
            # y : [[1,9],[3,4]]
        ```
* ``.deepcopy( )``
  *  ``deepcopy( )``는 ``깊은 복사``로 참조값 뿐만 아니라 참조하는 객체 자체를 복사한다. 원소 수준으로 복사하는 것이다.

        ```python
            import copy
            x = [[1,2],[3,4]]
            y = x.deepcopy()
            x[0][1] = 9
            # x : [[1,9],[3,4]]
            # y : [[1,2],[3,4]]
        ```
#### 3-2. 파이썬에서 인수 전달
파이썬에서 인수 전달은 ``실제 인수인 객체에 대한 참조를 값으로 전달``하여 매개변수에 대입되는 방식이다. 공식 문서에서는 이를 객체 ``참조에 의한 전달``(``call by object reference``)라고 정의한다. <br>
다른 프로그래밍 언어에서는 실제 인수의 값을 매개변수에 복사하는 값에 의한 호출(``call by value``)을 사용하거나, 실제 인수의 참조를 매개변수에 복사하여 매개변수가 실제 인수와 같아지는 참조에 의한 호출(``call by reference``)을 사용한다.
* 함수의 실행 시작 시점에서 매개변수는 실제 인수와 같은 객체를 참조한다. 함수에서 매개변수의 값을 변경하면 인수의 type에 따라 다음과 같이 구분한다.
  
  * 인수가 ``immutable``일 때
    * 함수 안에서 매개변수의 값을 변경하면 ``다른 객체를 생``성하고 그 객체에 대한 참조로 업데이트. 따라서 매개변수의 값을 변경해도 호출하는 쪽의 ``실제 인수에는 영향이 없다``.
  
  * 인수가 ``mutabl``e일 때
    * 함수 안에서 매개변수의 값을 변경하면 ``객체 자체를 업데이트`` 한다. 따라서 매개변수의 값을 변경하면 호출하는 쪽의 ``실제 인수는 값이 변경된다``.

### 4. mutable , immutable

### 5. 파이썬 모듈
 파이썬에선 하나의 스크립트 프로그램을 ``모듈``이라고 한다. 모듈 이름은 확장자( .py )를 뺀 ``파일의 이름`` 자체로 설정한다.(예: dodo.py면 dodo가 __name__이 됨) 
* 이때 해당 파일 안에서 함수를 실행시키면 ``__name__``은 ``__main__``이 된다.( 예: dodo.py 실행 시 __main__이 __name__이 됨 ) 
    ```python
        <dodo.py>

        def plus(a,b):
            print(f"{a + b} 모듈이름 : {__name__}")
        if __name__ == "__main__":
            plus(0,0)

        #실행 결과 -> 0 모듈이름 : __main__ 
    ```
* 반면 다른 파일에서 모듈을 import해서 사용하는 경우 ```__name__```엔 ```원래 모듈의 이름```이 담긴다.
    ```python
        <hoho.py>
        import dodo

        plus(2,4) # 6 모듈이름 : __dodo__
    ```
* ```if __name__ == "__main__" ```의 역할
  
  * ``__name__``은 파이썬에서 정한 이미 존재하는 변수다. 이 변수에 해당 파이썬의 파일의 이름( =모듈의 이름 )을 담게 된다. 즉 위의 if문이 의미하는 것은 해당 파일 안에서 함수를 실행시킬 때만 if문 안의 코드가 실행되게 하는 것이다. 즉 다른 파일에서 해당 파일을 import해서 사용하는 경우 if문 안의 코드는 실행되지 않는다. 
  
  * <dodo.py>의 if문을 지운 경우
    ```python
        <hoho.py>
        import dodo

        plus(2,4) # 0 모듈이름 : __dodo__
                  # 6 모듈이름 : __dodo__
    ```
### 6. 파이썬 예외처리
``FileNotFoundError``(디렉터리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류), ``ZeroDivisionError``( 0으로 다른 숫자를 나누는 경우 발생하는 오류),``IndexError``등의 오류가 발생하면 파이썬은 프로그램을 중단하고 오류 메시지를 보여 준다. 이를 무시하고 싶을 때 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.
#### 6-1. 오류 예외 처리 기법
* **try, except 문**

  ```python
    try:
        ...
    except[발생 오류[as오류 메세지 변수]]: #[]안의 내용은 생략 가능
        ...
    ```
    * **모두 생략 시** : 오류 종류에 상관 없이 오류 발생 시 except 블록 수행
    * **발생 오류만 포함 시** : 특정 오류가 발생했을 경우 except 블록 수행
    * **모두 표기 시** : 특정 오류가 발생했을 경우, 해당 오류의 에러 메세지를 메세지 변수를 통해 받을 수 있다. 이는 print(메세지 변수)를 통해 출력 가능하다.
    
#### 6-2. 오류 일부러 발생시키기
* 파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.
* 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해 종종 예외를 만들어 사용한다. 예외는 파이썬 내장 클래스인 Exception클래스를 상속하여 만들 수 있다.
```python
    class Myerror(Exception):
        pass
    def isZero(n):
        if n==0:
            raise Myerror()
        return n
    
    x = int(input())
    try:
        y = isZero(n)
        print(y)
    except Myerror:
        print("입력값이 0입니다") 
    
    # 0 => 입력값이 0입니다.
    # 1 => 1
```
### 7. [파이썬 언더바/언더스코어(_)의 의미](https://eine.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%96%B8%EB%8D%94%EB%B0%94%EC%96%B8%EB%8D%94%EC%8A%A4%EC%BD%94%EC%96%B4-%EC%9D%98-%EC%9D%98%EB%AF%B8%EC%99%80-%EC%97%AD%ED%95%A0)
* [python magic method](https://zzsza.github.io/development/2020/07/05/python-magic-method/)
---
#### 참고
- [파이썬에서 join 사용하기](https://blockdmask.tistory.com/468)
- [map_코딩도장](https://dojang.io/mod/page/view.php?id=2286)
- [sequence_코딩도장](https://dojang.io/mod/page/view.php?id=2205)
- [iterable_코딩도장](https://dojang.io/mod/page/view.php?id=2405)
- [if __name__ == "__main__"](https://lovelydiary.tistory.com/297)
- [얕은 복사,깊은 복사](https://wikidocs.net/16038)
- [예외처리](https://wikidocs.net/30)