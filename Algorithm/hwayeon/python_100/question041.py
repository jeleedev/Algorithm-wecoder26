# 소수판별

# 숫자가 주어지면 소수인지 아닌지 판별하는 프로그램을 작성해주세요.
# 소수이면 YES로, 소수가 아니면 NO로 출력해주세요.

# 소수 : 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수
# 음의 소수는 고려하지 않습니다.

# 답안
n = int(input())

def function(n):
    for i in range(2, n):
        if n % i == 0:
            return 'NO'
    return 'YES'

print(function(15))

# 답안
def check_prime(n):
    if n <= 1:
        return "NO"
    i = 2
    소수 = True
    while (i**2) < n:
        if n % i == 0:
            소수 = False
            break
        i += 1
    if 소수:
        return "YES"
    else:
        return "NO"

print(check_prime(1223))