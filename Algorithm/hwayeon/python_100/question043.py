# 10진수를 2진수로

# 우리가 흔히 사용하는 숫자 1, 8, 19, 28893 등등...은 10진수 체계입니다.
# 이를 컴퓨터가 알아 들을 수 있는 2진수로 바꾸려고 합니다. 어떻게 해야할까요?

# 예를 들어 13은 2^3 + 2^2 + 2^0 = 13 이기때문에 1101으로 표현합니다

# 사용자에게 숫자를 입력받고 이를 2진수를 바꾸고 그 값을 출력해주세요.
# (bin 함수를 사용하지 않고 풀어주세요.)

# 답안
n = int(input())

def function(n):
    list1 = []
    while n:
        list1.append(str(n % 2))
    n = n // 2
    list1.reverse()
    list1 = ''.join(list1)
    return int(list1)

# 답안
def function(n):
    res = []
    while n:
        res.append(str(n%2))
        n = n // 2
    return int(''.join(res[::-1]))

print(function(13))

# 답안
a = int(input())
b = []

while a:
    print(a)
    b.append(str(a % 2))
    a = int(a / 2)

b.reverse()
print(''.join(b))