## 🌈 힙(Heap) & 힙 정렬(Heap Sort)

## 힙(Heap) 구조란?
- 힙 자료구조는 완전 이진 트리를 기초로 하는 자료구조이다. 
  - 완전 이진트리는 마지막을 제외한 모든 노드에서 자식들이 꽉 채워진 이진트리를 뜻한다.
  
- 여러 개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다.

- 힙은 일종의 반정렬 상태(느슨한 정렬 상태) 를 유지한다. (큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도를 뜻 함)
간단히 말하면 부모 노드의 키 값이 자식 노드의 키 값보다 항상 크거나 작은 이진 트리를 말한다.

- 힙 트리에서는 중복 값을 허용한다. 

- 부모노드의 키값과 자식노드의 키값 사이에는 대소관계가 성립한다

![](https://images.velog.io/images/lck0827/post/3ebd2954-66f6-4b0c-869f-92ce525f11e9/image.png)

### 힙의 종류
1) **최대 힙(Max Heap)**
- 부모 키 값이 자식노드 키 값보다 큰 힙
  - Key(parent) ≥ Key(child)
- 가장 큰 값이 루트노드에 있음

2) **최소 힙(Min Heap)**
- 부모 키 값이 자식노드 키 값보다 작은 힙
  - Key(parent) ≤ Key(child)
- 가장 작은 값이 루트노드에 있음
![](https://images.velog.io/images/lck0827/post/c013fbc0-1a14-44e4-86c1-d5c1a730a394/image.png)


### 힙의 구현
- 힙을 저장하는 표준적인 자료구조는 배열 이다. 완전이진트리를 기본으로 하기 때문에 비었는 공간이 없어 배열로 구현하기에 용이하다.
- 구현을 쉽게 하기 위하여 배열의 첫 번째 인덱스인 0은 사용되지 않는다.
- 특정 위치의 노드 번호는 새로운 노드가 추가되어도 변하지 않는다.
(ex. 루트 노드의 왼쪽 노드의 번호는 항상 2이다)
- 힙에서의 부모 노드와 자식 노드의 관계
  - 왼쪽 자식의 인덱스 = (부모의 인덱스) * 2
  - 오른쪽 자식의 인덱스 = (부모의 인덱스) * 2 + 1
  - 부모의 인덱스 = (자식의 인덱스) / 2 (인덱스 0 사용 안하는 경우)

### 힙의 삽입(insert)
- 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 이어서 삽입한다.
새로운 노드를 부모 노드들과 교환해서 힙의 성질을 만족시킨다.

![](https://images.velog.io/images/lck0827/post/f3ff0f2d-fb53-480f-aef3-978ee1ac75cb/image.png)

```python
# Heap의 insert후 재구조화
def up_heapify(index, heap):
    child_index = index
    while child_index != 0:
        parent_index = (child_index-1) // 2
        if heap[parent_index] < heap[child_index]:
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            child_index = parent_index
        else : 
            return
```

### 힙의 삭제(delete)
- 최대 힙에서 최댓값은 루트 노드이므로 루트 노드가 삭제된다.
최대 힙(max heap)에서 삭제 연산은 최댓값을 가진 요소를 삭제하는 것이다.
삭제된 루트 노드에는 힙의 마지막 노드를 가져온다.
힙을 재구성한다.

![](https://images.velog.io/images/lck0827/post/b952224a-e919-468b-be23-e3a5d8146a1f/image.png)

```python
# Heap의 delete후 재구조화
def bigger_child(index, heap_size):
    parent = index
    left_child = (parent * 2) + 1
    right_child = (parent * 2) + 2

    if left_child < heap_size and heap[parent] < heap[left_child]:
        parent = left_child
    if right_child < heap_size and heap[parent] < heap[right_child]:
        parent = right_child
    return parent

def down_heapify(index, heap):
    parent_index = index
    bigger_child_index = bigger_child(parent_index, len(heap))
    while parent_index != bigger_child_index:
        heap[parent_index], heap[bigger_child_index] = heap[bigger_child_index], heap[parent_index]
        parent_index = bigger_child_index
        bigger_child_index = bigger_child_index(parent_index, len(heap))
```

---

## 힙 정렬(Heap Sort)
- 힙정렬의 시간복잡도는 O(NlogN)으로 빠른 정렬에 속한다. 퀵정렬은 최악의 경우 O(N<sup>2</sup>)의 성능을 내지만, 힙정렬은 안정적인 성능을 발휘한다. 또한 추가적인 배열을 사용하지 않아 메모리 측면에서도 이점이 있다. 

- 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 할 때 사용한다. 
  - 내림차순 정렬을 위해서는 최대 힙을 구성하고 오름차순 정렬을 위해서는 최소 힙을 구성하면 된다.



![](https://images.velog.io/images/lck0827/post/78567d76-6d10-4316-a289-98bc8a578088/image.png)


---

### 📝 Reference
1. https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
2. https://reakwon.tistory.com/42
3. https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%ED%9E%99Heap