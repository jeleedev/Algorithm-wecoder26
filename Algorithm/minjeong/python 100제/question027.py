# 문제27 : 딕셔너리 만들기

# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고, 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.

# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

# >> 입력
# Yujin Hyewon
# 70 100

# >> 출력
# {'Yujin': 70, 'Hyewon': 100}

key = list(input().split())
value = list(map(int, input().split()))

dict = {
    key[0] : value[0],
    key[1] : value[1]
}

print(dict)

# 답안

keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)

# zip은 두 개의 리스트를 서로 묶어줄 때 사용한다.
