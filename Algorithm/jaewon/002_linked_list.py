class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        if self.head == '':
            return None
        # 삭제할 Node가 self.head일 경우,
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next: # 우선 self.head는 아니기 때문에 self.head.next부터 확인
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next    

# 노드 생성
linkedlist = NodeMgmt(0)
linkedlist.desc()
for i in range(1,10):
    linkedlist.add(i)
# linkedlist.desc()
# for i in range(1,10):
#     linkedlist.delete(i)
# linkedlist.desc()
