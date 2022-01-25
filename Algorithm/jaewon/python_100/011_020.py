# 문제11 : for를 이용한 기본 활용
s = 0
n = 100
s = n*(n+1)// 2
print(s)


# 문제12 : 게임 캐릭터 클래스 만들기
class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()


# 문제13 : 몇 번째 행성인가요?
l = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
n = 1
# n = int(input())
print(l[n-1])


# 문제14 : 3의 배수 인가요?
def func(n):
    if n % 3:
        return n
    else: return '👏'
# user_input = int(input())    
user_input = 6
print(func(user_input))


# 문제15 : 자기소개
def func(name):
    return f"안녕하세요. 저는 {name}입니다."
# user_input = input()
user_input = "장재원"
print(func(user_input))


# 문제16 : 로꾸거
# data = input()
data = '거꾸로'
print(data[::-1])


# 문제17 : 놀이기구 키 제한
def func(height):
    if height > 150:
        return 'YES'
    else: return 'NO'
# user_input = int(input())
user_input = 150
print(func(user_input))


# 문제18 : 평균 점수
# l = sum(list(map(int, input().split())))/3
l = sum([50, 70, 80])/3
print(l)


# 문제19 : 제곱을 구하자
# l = list(map(int, input().split()))
l = [2, 5]
print(l[0] ** l[1])


# 문제20 : 몫과 나머지
# a,b = map(int, input().split())
a, b = 5, 2
print(a//b, a%b)
