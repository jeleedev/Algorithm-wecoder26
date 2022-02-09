# 대소문자 바꿔서 출력하기

# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.

# 입력
# AAABBBcccddd

# 출력
# aaabbbCCCDDD

# 답안
n = input()

def function(n):
    list1 = []
    for i in n:
        if i.isupper():
            list1.append(i.lower())
        else:
            list1.append(i.upper())
    return ''.join(list1)

# 답안
def function(n):
    list1 = []
    list2 = []
    for i in range(0, len(n)):
        list1.append(n[i])
        if list1[i].isupper() == True:
            list2.append(list1[i].lower())
        else: list2.append(list1[i].upper())
    return ''.join(list2)

# 답안
def function(n):
    n = list(n)
    list1 = []
    for i in n:
        if i.isupper():
            list1.append(i.lower())
    else: list1.append(i.upper())
    return ''.join(list1)

# 답안
a = input()
b = []

for i in a:
	if i.islower():
		b.append(i.upper())
	else:
		b.append(i.lower())
	
for i in b:
	print(i, end='')

print(function(n))