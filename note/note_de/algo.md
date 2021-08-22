# ✏️알고리즘 노트


## 1. 다이나믹 프로그래밍(Dynamic Programming)

* 다이나믹 프로그래밍은 '하나의 문제는 단 한번만 풀도록 하는 알고리즘'이다.

* 다음의 조건을 만족할 때 사용 가능하다
    * 최적 부분 구조
      * 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
    * 중복되는 부분 문제
      * 동일한 작은 문제를 반복적으로 해결해야 한다.
* 점화식으로 나타낼 수 있다.
  * 예) 피보니치 수열의 점화식 : ``dp[N] = dp[N-1] + dp[N-2]``

#### 예시) 피보나치 수열

![사진](https://github.com/coding-study-19/datastructure-and-algorithm/blob/main/note/note_de/img/fibo.PNG?raw=true)
* **단순한 <U>분할 정복</U> 기법을 이용해 피보나치 수열을 구할 경우**
    ```python
        def fibo(x):
            if x==1 : return 1
            if x==2 : return 1
            return fibo(x-1) + fibo(x-2)
        fibo(15)
    ```


  * 이미 해결한 문제를 다시 반복적으로 해결하여 비효율적이다.( fibo(12)를 3번이나 계산한다. )
  * 시간 복잡도 : O(2^N)
  
* **<U>다이나믹프로그래밍</U> 기법을 이용해 피보나치 수열을 구할 경우**
  * 큰 문제를 작은 문제로 나눌 수 있고, 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
  * ``memozation``기법
  
    * 이미 <U>계산한 결과는 배열에 저장</U>함으로써 나중에 동일한 계산을 해야 할 때는 저장된 값을 단순히 반환하기만 하면 된다.
  
    ```python
        arr = [0]*100 #memozation

        def fibo(x):
            if x==1 : return 1
            if x==2 : return 1
            if arr[x]!=0 return d[x] #중복되는 부분 해결
            return fibo(x-1) + fibo(x-2)
        fibo(15)
    ```
    * 이미 계산된 결과는 arr에 저장되기 때문에 한번 구한 값을 다시 구하지 않는다.

---
* 관련 문제

#### 참고
- [다이나믹 프로그래밍](https://blog.naver.com/ndb796/221233570962)

