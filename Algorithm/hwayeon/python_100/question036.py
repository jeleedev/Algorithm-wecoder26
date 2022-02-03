# 구구단 출력하기

# 1~9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램을 작성하세요.

# 답안
def multiplication(n):
    for i in range(1,10):
        print(n * i, end=' ')

n = 2
multiplication(n)

# 답안
n = int(input())
for i in range(1, 10):
	print(n*i, end = ' ')