# count 사용하기

# 학기를 맞아 호준이네 반은 반장 선거를 하기로 했습니다. 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 하였습니다.

# 입력
# 원범 원범 혜원 혜원 혜원 혜원 유진 유진

# 출력
# 혜원(이)가 총 4표로 반장이 되었습니다.

# 답안
n = input()
list1 = n.strip().split()
name = max(list1)
count_name = list1.count(name)

print (f'{max(list1)}(이)가 총 {count_name}표로 반장이 되었습니다.')

# 답안
n = input()
list1 = n.strip().split()
list2 = list(set(list1))

num = 0
res = ''
for i in list2:
    temp_count = list1.count(i)
    if num < temp_count:
        num = temp_count
        res = i
print(f'{res}(이)가 총 {num}표로 반장이 되었습니다.')

# 답안
data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')