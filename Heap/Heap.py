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