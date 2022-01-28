# 문제33 : 거꾸로 출력하기

# 한 줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성하시오.

# >>입출력

# 입력 : 1 2 3 4 5
# 출력 : 5 4 3 2 1

# 입력 : 2 4 6 7 8
# 출력 : 8 7 6 4 2

n = list(map(int, input().split()))
n_reverse = n[::-1]

print(" ".join(map(str, n_reverse)))

# 답

n = input()

l = list(n.strip().split())
len1 = len(l) - 1
for i in range(len1, -1, -1):
	print(l[i], end=' ')