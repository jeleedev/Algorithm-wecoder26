# 거꾸로 출력하기

# 한 줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성하시오.

# 입력 : 1 2 3 4 5
# 출력 : 5 4 3 2 1

# 입력 : 2 4 6 7 8
# 출력 : 8 7 6 4 2

# 답안
n = input()
list1 = n.strip().split()
reverse_list1 = list1[::-1]
print(' '.join(reverse_list1))

# '구분자'.Join(): 리스트의 문자열 요소들을 하나로 합치는 메서드

# 답안
n = '1 2 3 4 5'
list1 = n.strip().split()
reverse_list1 = reversed(list1)
print(' '.join(list(reverse_list1)))

# 답안
n = input()
list1 = list(map(str, n.strip().split()))
reverse_list1 = list1[::-1]
print(' '.join(reverse_list1))

# 답안
l = list(n.strip().split())
len1 = len(l) - 1
for i in range(len1, -1, -1):
	print(l[i], end=' ')