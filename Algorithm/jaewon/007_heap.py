# heap 데이터 삽입
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 맨 앞에 요소는 None으로 채움
        self.heap_array.append(data)
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # inserted_idx가 Root Node일 경우
            return False
        parent_idx = inserted_idx // 2
        # inset한 Node의 값이 insert한 Node의 parent의 Data값 비교
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False
    # 완전 이진트리의 규칙으로 배열에 Node 값 삽입
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        # Swap
        inserted_idx = len(self.heap_array) - 1 # 최근 추가된 데이터의 index 번호
        # move_up 매서드에 inserted_idx값을 전달하였을 때, True가 return되면 계속 반복
        while self.move_up(inserted_idx): 
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap
            inserted_idx = parent_idx
        return True
# 데이터 삽입 확인        
heap = Heap(15)
print(heap.heap_array) # [None, 15]
heap.insert(10)
print(heap.heap_array) # [None, 15, 10]
heap.insert(8)
print(heap.heap_array) # [None, 15, 10, 8]
heap.insert(5)
print(heap.heap_array) # [None, 15, 10, 8, 5]
heap.insert(4)
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.insert(20)
print(heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]