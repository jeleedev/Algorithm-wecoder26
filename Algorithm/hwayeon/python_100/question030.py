# 문자열 속 문자 찾기

# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다. 원범이는 이렇듯 문자열 속에 숨어있는 문자를 찾아보려고 합니다.

# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면 
# 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요

# 입력
# pineapple is yummy
# apple

# 출력
# 4

# 답안
data = 'pineapple is yummy'
target = 'apple'

print(data.find(target))

# find 함수

# string.find(찾을 문자, 시작 Index, 끝 Index)
# : find 함수는 먼저 찾을 문자나 문자열이 존재하는지 확인하고, 
#   존재한다면 해당위치의 index를 반환하고 존재하지 않으면 -1을 반환
#   만약 찾는 문자나 문자열이 여러개 있다면 맨 처음 찾은 문자의 index를 반환

# 답안
def findIndex(data, target):
    for i in range(len(data)-len(target)):
        if data[i:i+len(target)] == target:
            return i

print(findIndex(data, target))

# 답안
def index_find(data, target):
    i = 0
    if target not in data:
        return -1
    while True:
        if data[i:i+len(target)] == target:
            return i
        else:
            i += 1

print(index_find(data, target))