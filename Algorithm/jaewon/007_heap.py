class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # inseted_inx가 Root Node일 경우
            return False
        parent_idx = inserted_idx // 2
        # inset한 Node의 값이 inset한 Node의 parent의 Data값 비교
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
    # Root Node 삭제
    def move_down(self, poped_idx):
        left_child_poped_idx = poped_idx * 2
        right_child_poped_idx = poped_idx * 2 + 1
        # case1 : 왼쪽 자식 노드가 없을때(자식 Node가 모두 없다는 의미)
        if left_child_poped_idx >= len(self.heap_array):
            return False
        # csee2 : 왼쪽 자식 노드만 있을 때(오른쪽 자식 노드는 없음)
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                return True # 자식이 더 클 때는 Swap(While문 실행)
            else:
                return False
        # csee3 : 왼쪽, 오른쪽 자식 노드가 모두 있을 때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False
    def pop(self):
        # Node가 없거나(비어있는 이진 트리), Root Node만 있는 경우
        if len(self.heap_array) <= 1: 
            return None
        returned_data = self.heap_array[1] # 첫번째 Node의 값(Root Node의 value)
        # Swap
        self.heap_array[1] = self.heap_array[-1] # 마지막 데이터를 Root Node로 교체
        del self.heap_array[-1] # Root Node로 이동했기 때문에 삭제
        poped_idx = 1
        while self.move_down(poped_idx): # move_down 메서드를 통해 True를 반환 받으면 반복문 실행
            left_child_poped_idx = poped_idx * 2
            right_child_poped_idx = poped_idx * 2 + 1
            # csee2 : 왼쪽 자식 노드가 있을 때
            if right_child_poped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_poped_idx
            # csee3 : 왼쪽, 오른쪽 자식 노드가 모두 있을 때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx], self.heap_array[poped_idx]
        return returned_data
# 데이터 삽입 확인        
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.insert(20)
print(heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]
# 데이터 삭제 확인
heap.pop()
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.pop()
print(heap.heap_array) # [None, 10, 4, 8, 5]
heap.pop()
print(heap.heap_array) # [None, 8, 4, 5]

# heap 데이터 삭제
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # inseted_inx가 Root Node일 경우
            return False
        parent_idx = inserted_idx // 2
        # inset한 Node의 값이 inset한 Node의 parent의 Data값 비교
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
    # Root Node 삭제
    def move_down(self, poped_idx):
        left_child_poped_idx = poped_idx * 2
        right_child_poped_idx = poped_idx * 2 + 1
        # case1 : 왼쪽 자식 노드가 없을때(자식 Node가 모두 없다는 의미)
        if left_child_poped_idx >= len(self.heap_array):
            return False
        # csee2 : 왼쪽 자식 노드만 있을 때(오른쪽 자식 노드는 없음)
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                return True # 자식이 더 클 때는 Swap(While문 실행)
            else:
                return False
        # csee3 : 왼쪽, 오른쪽 자식 노드가 모두 있을 때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False
    def pop(self):
        # Node가 없거나(비어있는 이진 트리), Root Node만 있는 경우
        if len(self.heap_array) <= 1: 
            return None
        returned_data = self.heap_array[1] # 첫번째 Node의 값(Root Node의 value)
        # Swap
        self.heap_array[1] = self.heap_array[-1] # 마지막 데이터를 Root Node로 교체
        del self.heap_array[-1] # Root Node로 이동했기 때문에 삭제
        poped_idx = 1
        while self.move_down(poped_idx): # move_down 메서드를 통해 True를 반환 받으면 반복문 실행
            left_child_poped_idx = poped_idx * 2
            right_child_poped_idx = poped_idx * 2 + 1
            # csee2 : 왼쪽 자식 노드가 있을 때
            if right_child_poped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                    poped_idx = left_child_poped_idx
            # csee3 : 왼쪽, 오른쪽 자식 노드가 모두 있을 때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx], self.heap_array[poped_idx]
        return returned_data
# 데이터 삽입 확인        
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.insert(20)
print(heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]
# 데이터 삭제 확인
heap.pop()
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.pop()
print(heap.heap_array) # [None, 10, 4, 8, 5]
heap.pop()
print(heap.heap_array) # [None, 8, 4, 5]
