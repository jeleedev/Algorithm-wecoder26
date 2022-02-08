# 문제38 : 호준이의 아르바이트

# 호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다.
# 호준이가 일하는 학원은 매번 1위부터 3위까지의 학생에게 상으로 사탕을 준다.
# 그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고 점수를 보내면,
# 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.

# 학생들의 점수를 공백으로 구분하여 입력받는다.
# 1위~3위 학생은 여러명일 수 있고 1~3위 학생 중 중복되는 학생까지 포함하여 사탕을 사기로 한다.

# - 학생 수는 4명 이상입니다.
# - 숫자 외에 다른 값은 입력되지 않습니다.

# 점수입력 : 97 86 75 66 55 97 85 97 97 95
# 출력 : 6

data = input().split()
data = [int(i) for i in data]

count = 0
# print(f'data : {data}')
# print(f'set(data) : {set(data)}')
if len(set(data)) <= 3:
    count = len(data)
else:
    break_point = sorted(list(set(data)), reverse=True)[3]
    # print(f'reverse_sorted_data : {sorted(list(set(data)), reverse=True)}')
    # print(f'break_point : {break_point}')
    data_sorted = sorted(data, reverse=True)
    # print(f'data_sorted : {data_sorted}')
    for i in data_sorted:
        if break_point == i:
            break
        else:
            count += 1

print(count)

# data : [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]
# set(data) : {97, 66, 75, 85, 86, 55, 95}
# reverse_sorted_data : [97, 95, 86, 85, 75, 66, 55]
# break_point : 85
# data_sorted : [97, 97, 97, 97, 95, 86, 85, 75, 66, 55]

# sorted 함수
# https://blockdmask.tistory.com/466