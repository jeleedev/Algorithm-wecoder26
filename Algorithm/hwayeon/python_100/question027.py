# 딕셔너리 만들기

# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고, 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

# 입력
# Yujin Hyewon
# 70 100

# 출력
# {'Yujin': 70, 'Hyewon': 100}

# 답안
key = list(input().split())
value = list(map(int, input().split()))

print(dict(zip(key, value))) # zip 함수 사용

# zip() 함수란
# 여러 개의 iterable 자료형이 개수가 동일할 때 각각의 요소를 나눈 후 순서대로 묶어서 요소 개수만큼 새로운 iterable 자료형을 생성한다.
# (여기에서 말하는 interable 자료형은 리스트, 튜플 같이 반복 가능한 자료형을 의미)

# 답안
keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)