## 🌈 스택(Stack) & 큐(Queue)에 대하여

> **스택과 큐는 자료구조에서 가장 기본적이면서도 중요하게 소개된다. 
알고리즘 문제를 풀다보면 스택과 큐의 개념을 정확하게 모르면서 코드 작성을 하기도하고 자연스럽게 구현이 되는 경우도 있다. 
우리가 인지하지 못하는 부분에서 많이 구현이 되는 개념이기 때문에 정확하게 알아보도록 하자 **

## 스택(Stack)이란?
- 스택(stack)이란 쌓아 올린다는 것을 의미한다. 데이터를 차곡차곡 쌓아올린 형태이며, 가장 마지막에 삽입된 데이터가 가장 먼저 삭제되는 구조를 가지고 있다. 

![](https://images.velog.io/images/lck0827/post/a4689089-ff15-4ffe-bb0b-1a65641f0937/image.png)

### 스택의 특징
- 정해진 방향으로만 데이터를 쌓을 수 있다. 
- top으로 정한 곳을 통해서만 데이터 삽입이 가능하다.
- 삽입은 'PUSH', 삭제는 'POP' 이라는 용어를 사용한다.
- **후입선출(LIFO, Last-In-First-Out)** 구조이다.

😡 **스택 오버 플로우**
![](https://images.velog.io/images/lck0827/post/cbe9f056-8c87-4b59-ba34-a2d1f28c5586/image.png)
👉 데이터를 계속 삽입하다가 수용 가능한 크기를 초과해서 흘러넘치는 경우를 의마한다. 재귀 호출시 자주 경험한다. 

### 시간 복잡도
- Insertion O(1)
- Deletion O(1)
- Search O(n)

### 스택의 사용사례
- 웹 브라우저의 '뒤로가기' 기능
- 문서 작업에서 ctrl + z (되돌리기) 기능
- 역순 문자열 만들기

---

## 큐(Queue)란?
- 스택의 반대개념이며, Queue 의 사전적 의미는 '줄' 혹은 '줄을 서서 기다리는 것'을 의미한다.


![](https://images.velog.io/images/lck0827/post/943ec3e0-cf1b-45ff-a5f2-ed8de5b4c31e/image.png)

### 큐의 특징
- 스택과는 달리, 큐는 한쪽 끝에서 삽입이, 다른 쪽 끝에서 삭제가 작업이 양쪽으로 이루어진다.
- 큐의 가장 첫 원소를 'front' 가장 끝 원소를 'rear' 라고 한다.
- 큐의 리어에서 이루어지는 삽입연산을 인큐(enQueue), 프론트에서 이루어지는 삭제연산을 디큐(dnQueue)라고 부른다.
- 선입선출(FIFO, First in first out) 방식의 자료구조

### 시간 복잡도
- Insertion O(1)
- Deletion O(1)
- Search O(n)

### 큐의 사용사례
👉 **주로 순서를 보장하기 위한 처리를 해야할 때 사용된다. **
- 우선순위가 같은 작업 예약 (프린터의 인쇄 대기열)
- 은행 업무
- 콜센터 고객 대기시간
- 프로세스 관리
- 너비 우선 탐색(BFS, Breadth-First Search) 구현
- 캐시(Cache) 구현

---

### 📝 Reference
1. https://mygumi.tistory.com/357
2. https://devuna.tistory.com/22
