<정리>
* deque : (https://appia.tistory.com/203)
* 얕은 복사 vs 깊은 복사 : (https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/)
* 인덱스 위치 : (https://ooyoung.tistory.com/78)
* 슬라이스 : (https://nirsa.tistory.com/41)
* 값 삭제 : (https://ponyozzang.tistory.com/587)
* filter : (https://blockdmask.tistory.com/532) , (https://www.daleseo.com/python-filter/)
# ✏️노트
---
## 📊파이썬 함수

### 1. join 함수
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


### 2. map 함수
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
---
## 📌파이썬 개념
파이썬에서 중요한 개념 중에 하나가 "반복 가능한(iterable)"이다.
 어떤 메서드를 쓸 수 있냐, 업냐 는 해당 객체가 ```반복 가능한지```, ```시퀀스```인지에 따라 나뉜다. 공통 속성을 갖고 있다면 해당 기능을 쓸 수 있다.

시퀀스 객체야? 그러면 in을 쓸 수 있겠네?
반복 가능한 객체야? 그러면 for를 쓸 수 있겠네?

이렇게 생각할 수 있다. 따라서 문자열 따로, 리스트 따로, 튜플 따로 학습하는 것이 아니라 파이썬 표준에서 제시하는 기본 개념인 반복 가능한과 시퀀스를 이해하는 것이 중요하다.

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
  
    ![사진](https://dojang.io/pluginfile.php/13952/mod_page/content/3/039002.png)
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

---
#### 출처
- [파이썬에서 join 사용하기](https://blockdmask.tistory.com/468)
- [map_코딩도장](https://dojang.io/mod/page/view.php?id=2286)
- [sequence_코딩도장](https://dojang.io/mod/page/view.php?id=2205)
- [iterable_코딩도장](https://dojang.io/mod/page/view.php?id=2405)