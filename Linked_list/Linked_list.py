class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class Linkedlist:
    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        delete_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before # 중요 : current가 next가 아닌 before로 변경된다.
        #

        self.num_of_data -= 1

        return delete_data

    # first 메소드 (search - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0: # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # next 메소드 (search - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    # size 메소드
    def size(self):
        return self.num_of_data

if __name__ == '__main__':
    linkedlist = Linkedlist()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(4)
    linkedlist.append(5)
    linkedlist.append(6)
    linkedlist.append(7)

print(linkedlist.first())       # 1
print(linkedlist.next())        # 2
print(linkedlist.size())        # 7
print(linkedlist.delete())      # 2
print(linkedlist.size())        # 6
print(linkedlist.current.data)  # 1
print(linkedlist.tail.data)     # 7
print(linkedlist.first())       # 1
print(linkedlist.next())        # 3
print(linkedlist.next())        # 4
print(linkedlist.next())        # 5