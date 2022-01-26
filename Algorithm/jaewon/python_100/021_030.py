# 문제21 : set은 어떻게 만드나요?
"""
1)  x = {1, 2, 3, 5, 6, 7} => O
2)  x = {} => X
3)  x = set('python') => O
4)  x = set(range(5)) => O
5)  x = set() => O
"""

# 문제22 : 배수인지 확인하기
"""
1)  i / 6 == 0 => X
2)  i % 6 == 0 => O
3)  i & 6 == 0 => X
4)  i | 6 == 0 => X
5)  i // 6 == 0 => X
"""

# 문제23 : OX문제
# print(10/2)의 출력 결과는 5이다. => X


# 문제24 : 대문자로 바꿔주세요!
# user_input = input()
user_input = 'mary'
print(user_input.upper())


# 문제25 : 원의 넓이를 구하세요
def func(r):
    return r ** 2 * 3.14
# user_input = int(input())
user_input = 10
print(func(user_input))


# 문제26 : 행성 문제2
# kor_l = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# eng_l = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# d = {}
# for i in range(len(kor_l)):
#     d[kor_l[i]] = eng_l[i]
# user_input = input() 
# print(d[user_input])

# user_input = input()
user_input = '수성'
kor_l = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
eng_l = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
d = dict(zip(kor_l, eng_l))
print(d[user_input])


# 문제27 : 딕셔너리 만들기
name_l = ['Yujin', 'Hyewon']
score_l = [70, 100]
# name_l = input().split()
# score_l = list(map(int, input().split()))
res = dict(zip(name_l, score_l))
print(res)


# 문제28 : 2-gram
data = 'Python'
for i in range(len(data)-1):
    print(data[i:i+2])


# 문제29 : 대문자만 지나가세요    
def func(data):
    if data.isupper():
        return 'YES'
    else: return 'NO'
# data = input()
data = 'A'
print(func(data))

def func(data):
    res = [i for i in data if i.isupper()]
    return res
# data_l = input().split()
data_l = ['A', 'C', 'b', 'Z', 'f']
print(func(data_l))


# 문제30 : 문자열 속 문자 찾기
# data = input()
# target = input()
data = 'pineapple is yummy'
target = 'apple'
print(data.find(target))

def func(data, target):
    i = 0
    if target not in data:
        return None
    while True:
        if data[i:i+len(target)] == target:
            return i
        else: i+=1
        
data = 'pineapple is yummy'
target = 'apple'
print(func(data, target))