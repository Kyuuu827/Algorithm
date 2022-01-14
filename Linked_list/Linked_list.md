## 🌈 연결 리스트(Linked List)

## 연결 리스트 란?
- 연결 리스트는 노드들로 이어진 리스트를 의미한다.

- 노드는 데이터를 저장하는 부분과, 다음 노드를 가르키는 부분으로 구성되어있다. 

- 연결 리스트는 처음과 끝을 가르키는 포인터들을 이용해 리스트를 관리하고, 끝 노드는 null값을 가지고 있다.

- 제일 앞에 있는 노드는 헤드(head), 제일 끝 노드는 테일(tail)이라고 부른다. 아무 데이터가 없는 노드는 더미노드 라고 부른다. 

- linked list에서 가장 중요한 것은 연결이 무엇인가를 파악하는 것이다.

- 연결되는 방향에 따라 단일 연결 리스트(Single Linked List), 이중 연결 리스트(Double Linked List), 원형 연결 리스트(Circular Linked List)의 종류가 있다. 

- python 의 경우 list 기본 자료형에 linked list 기능이 함께 포함되어 있다.

![](https://images.velog.io/images/lck0827/post/19c874e5-7c32-4c58-8060-c2f6d864f7dc/image.png)

### 연결 리스트의 장점
- 연결 리스트의 길이를 동적으로 조절 가능하다.
- 데이터의 삽입과 삭제가 쉽다.

### 연결 리스트의 단점
- 임의의 노드에 바로 접근할 수 없다.
- 다음 노드의 위치를 저장하기 위한 추가 공간이 필요하다.
- Cache locality를 활용해 근접 데이터를 사전에 캐시에 저장하기가 어렵다. 
- 연결 리스트를 거꾸로 탐색하기가 어렵다

👉 데이터가 자주 추가되거나 가변적으로 자주 변하게 될 프로그램이라면 링크드리스트를 쓰는 것이 효율적이고, 주로 데이터의 변경이나 탐색을 위한 것이라면 배열을 쓰는 것이 좋다.

---
## 이중 연결 리스트(Double Linked List)

- 단순 연결 리스트는 선행 노드에 접근하기가 어렵다. 그래서 이를 개선하기 위해 원형 연결 리스트를 구성했지만, 원형 연결 리스트에서도 현재 노드의 선행 노드에 접근하기 위해서는 전체 리스트를 한바퀴 순회해야 하는 문제가 생긴다.
이러한 문제점들을 보완하기 위해 이중 연결 리스트(Doubly Linked List)가 있다.

- 이중 연결 리스트는 각 노드가 선행 노드와 후속 노드에 대한 링크를 가지는 리스트이다. 

- 노드의 왼쪽 링크(left link)와 오른쪽 링크(right link)가 각각 다른 노드의 오른쪽 링크와 왼쪽 링크를 연결짓고 있으며 헤드도 노드로 이루어져 있다. 

![](https://images.velog.io/images/lck0827/post/c76f0eb1-7cf4-47bc-8394-1dfed53921b7/image.png)

---

## 원형 연결 리스트(Circular Linked List)

- 원형 연결 리스트는 이 전에 해왔던 단일 연결 리스트나 이중 연결 리스트에서 끝을 처음과 연결된 리스트이다.

- 원형 리스트는 모든 포인터가 다음 노드로 연결되어 있다.
즉, 마지막에서 첫번째로 이동하지 않아도 다음 노드가 첫번째 노드를 가리킨다. 

![](https://images.velog.io/images/lck0827/post/71150b4d-c112-4697-bddc-75fe1cb24f2d/image.png)

---

### 📝 Reference
1. https://cocoon1787.tistory.com/84
2. https://daimhada.tistory.com/72
3. https://reakwon.tistory.com/25
4. https://velog.io/@qkrcndtlr123/Linked-List
5. https://opentutorials.org/module/1335/8940