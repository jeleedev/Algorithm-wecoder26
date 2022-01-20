#stack - FILO
def stack_push(stack, value):
    stack.append(value)
def stack_pop(stack):
    last = stack.pop()
    return last
# 배열 생성
stack = []
# push
stack_push(stack, 5)
stack_push(stack, 6)
stack_push(stack, 7)
stack_push(stack, 8)
print(stack) # [5, 6, 7, 8]
# pop
last = stack_pop(stack)
print(last) # 8 
print(stack) # [5, 6, 7]


#queue - FIFO
from queue import deque
# push
def queue_push(q, value):
    q.append(value)
# pop
def queue_pop(q):
    front = q.popleft()
    return front
# 호출
queue = deque()
queue_push(queue, 5)
queue_push(queue, 6)
queue_push(queue, 7)
queue_push(queue, 8)
front = queue_pop(queue)
print(front) # 5
print(list(queue)) # [6, 7, 8]