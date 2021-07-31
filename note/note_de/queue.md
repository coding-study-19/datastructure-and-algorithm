# ✏️노트


## 파이썬에서 큐(queue) 자료구조 사용 방법

파이썬에서 큐 자료구조를 사용하는 방법은 3가지 정도가 있다.
1. ```list``` 자료구조 사용
2. collection 모듈의 ```deque``` 사용
3. queue 모듈의 ```Queue``` 클래스 사용

### 1. list
* pop(0) 
  * list객체의 함수로, 첫번째 데이터를 제거한다.
* append( )
  * list객체의 함수로, 새로운 데이터를 삽입한다.
  ```python
      queue = [4, 5, 6]
      queue.append(7)
      queue.append(8)
      #queue [4, 5, 6, 7, 8]
      queue.pop(0)
      4
      queue.pop(0)
      5
      #queue [6, 7, 8]
    ```
* insert(0,x)
    * 큐 자료구조를 사용하고 싶다면 이 함수를 통해 맨 앞에 데이터를 삽입할 수 있다.
    ```python
        queue = [4,5,6]
        queue.insert(0,3)
        queue.insert(0,2)
        #queue [2,3,4,5,6]
    ```
* [성능]
    * 파이썬의 ```list```는 다른 언어의 배열처럼 무작위 접근(random access)에 최적화된 자료 구조이기 때문에 ```pop(0)```또는 ```insert(0, x)```는 성능적으로 매우 불리한 연산이다. 이 두 연산은 시간 복잡도는 ```O(N)```이기 때문에 담고 있는 데이터의 개수가 많아질 수록 느려진다. 데이터의 삽입이나 삭제 후 남아있는 모든 데이터를 이동시켜야 하기 때문이다. 
### 2. deque
```collections``` 모듈의 ```deque```는 double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료 구조다. 

```deque```는 ```list```에는 없는 ```popleft()```메서드를 제공한다.
* deque 불러오기
    ```python
        from collections import deque
        queue = deque()
    ```
* popleft( )
    * 첫번째 데이터를 제거한다.
    * list의 pop(0)과 동일
* append( )
  * 새로운 데이터를 삽입한다.
  ```python
      queue = deque()

      queue.append(4)
      queue.append(5)
      queue.append(6)
      # queue deque([4,5,6])
      queue.popleft()
      queue.popleft()
      # queue deque([6])
  ```
* appendleft(x)
  * 맨 앞에 데이터를 삽입한다
  * list의 insert(0,x)와 동일
   ```python
       queue = deque([5,6,7])

       queue.appendleft(4)
       queue.appendleft(3)
       queue.append(2)
       # queue deque([2,3,4,5,6])
  ```
* [성능]
  * ```deque```의 ```popleft()```와 ```appendleft(x)```메서드는 모두 O(1)의 시간 복잡도를 가지기 때문에, ```list```의 ```pop(0)```와 ```insert(0, x)``` 대비 성능 상에 큰 이점이 있다.
  
  * 하지만 무작위 접근(random access)의 시간 복잡도가 ```O(N)```이라는 점과 내부적으로 linked list를 사용한다는 점으로 인해 i 번째 데이터에 접근하려면 맨 앞/뒤부터 i 번 순회(iteration)가 발생하게 된다.

### 3. Queue
```queue``` 모듈의 ```Queue```클래스는 주로 멀티 쓰레딩(threading) 환경에서 사용되며, 내부적으로 라킹(locking)을 지원하여 여러 개의 쓰레드가 동시에 데이터를 추가하거나 삭제할 수 있다.

```deque```와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리됩니다
* Queue 불러오기
    ```python
        from queue import Queue
        que = Queue()
    ```
* put( )
  * 데이터 추가
* get( )
  * 데이터 삭제
  ```python
      que = Queue()
      que.put(4)
      que.put(5)
      que.put(6)
      # 4,5,6
      que.get() # 4
      que.get() # 5
    ```
* [성능]
    * ```Queue```의 성능은 ```deque```와 마찬가지로 데이터 추가/삭제는 ```O(1)```, 데이터 접근은 ```O(N)```의 시간 복잡도를 가진다.
---
* 관련 문제
    * [백준 10845번](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/datastructure/%ED%81%90/10845_de.py)
---
#### 출처
- [파이썬에서 큐 자료구조 사용하기](https://www.daleseo.com/python-queue/)
- [deque](https://docs.python.org/3.8/library/collections.html#collections.deque)
- [queue](https://docs.python.org/3/library/queue.html)

