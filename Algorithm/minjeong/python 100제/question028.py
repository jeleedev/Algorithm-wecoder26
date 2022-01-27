# 문제28 : 2-gram

# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다. 
# 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.

# >> 출력
# Py
# yt
# th
# ho
# on

# 입력으로 문자열이 주어지면 2-gram으로 출력하는 프로그램을 작성해 주세요.

text = input()

for i in range(len(text) - 1):
    print(text[i], text[i + 1], sep='')

text2 = input()

two_gram = zip(text2, text2[1:])
for i in two_gram:
    print(i[0], i[1], sep='')

# list(zip(text, text[1:]))
# [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]

# 답안

data = input()

for i in range(len(data) - 1):
	print(data[i], data[i+1], sep = '')