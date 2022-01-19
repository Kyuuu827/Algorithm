## 🌈 이진 탐색 트리(Binary Search Tree)

- 이진 탐색(binary search)과 연결리스트(linked list)를 결합한 자료구조이다. 
- 이진 탐색의 효율적인 탐색 능력의 장점을 유지하면서 빈번한 자료 입력과 삭제가 가능하다. 

  ✔ 이진 탐색 
  - 탐색 시간복잡도는 O(log n), 
  - 자료 입력, 삭제 불가능
  
  ✔ 연결리스트 
  - 탐색 시간복잡도는 O(n)
  - 자료 입력, 삭제의 시간복잡도 O(1)

![](https://images.velog.io/images/lck0827/post/9ca4808f-6ff9-4eac-bc7a-9fcaf44949b1/image.png)


![](https://images.velog.io/images/lck0827/post/6d44a293-da06-46d2-8bce-e1ab712a00b7/image.png)

- 이진탐색트리를 순회할 때는 중위순회(inorder) 방식을 쓴다.(왼쪽 서브트리-노드-오른쪽 서브트리 순으로 순회)
- 위의 그림을 중위 순회하면, 4, 10, 12, 15, 17, 19, 20, 26, 28, 30, 33, 35 가 된다. 