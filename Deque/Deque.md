## 🌈 덱(deque)에 대하여


## 덱(deque)이란?
- 큐의 전단(front)와 후단(rear)에서 모두 삽입과 삭제가 가능한 큐 이다. 
- 스택과 큐를 동시에 사용 가능하다. 

![](https://images.velog.io/images/lck0827/post/a77beebc-dad6-4ca6-9e20-136f09b60922/image.png)

### 덱의 특징
- 덱은 일반적인 큐와 마찬가지로 데이터의 삽입 삭제를 수행하는 자료구조이다.
- 덱은 rear와 front 어느 곳에서든 삽입 삭제가 모두 이루어 질 수 있다.

- 덱의 연산은 크게 push(데이터 삽입), pop(데이터 삭제)으로 나뉜다.
  - **push()**
Queue와 같은 형태로 데이터를 덱에 삽입하는 연산이지만 양방향에서 원하는 곳으로 데이터 삽입 가능
  - **pop()**
데이터를 덱에서 삭제하는 연산
rear와 front 모두에서 데이터를 삭제 가능
- 크기가 가변적이고 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.
- 원하는 요소에 바로 접근이 가능하다.
- 구현이 어렵고 데이터의 중간 삽입, 삭제가 용이하지 않다는 단점이 있다.

### 시간 복잡도
- Insertion O(1)
- Deletion O(1)
- **Search O(1)**
👌 검색 연산의 경우, 덱에 있는 데이터에 인덱스로 접근하기 때문에 시간복잡도는 O(1)이 된다.

### 덱의 사용
- 주로 데이터가 가변적일 때 사용된다. 
- 많은 경우에서 덱은 리스트보다 우월한 옵션이다.
- push/pop이 빈번한 알고리즘에서 리스트보다 월등한 속도를 확인할 수 있다. 

---

### 📝 Reference
1. https://honggom.tistory.com/39
2. https://leonkong.cc/posts/python-deque.html