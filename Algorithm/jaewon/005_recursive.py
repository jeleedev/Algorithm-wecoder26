# 리스트합(for문)
def sum_l_for(l):
    res = 0
    for i in l:
        res += i
    return res
l = [1,2,3,4,5,6,7,8,9,10]
print(sum_l_for(l))

# 리스트합(재귀)
def sum_l_recursive(l):
    if len(l) <= 1: return l[0]
    return l[0] + sum_l_recursive(l[1:])
l = [1,2,3,4,5,6,7,8,9,10]
print(sum_l_recursive(l))

# 팩토리얼(for문)
def factorial(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  return res
print(factorial(5)) # 120

# 팩토리얼(재귀)
def factorial(n):
  if n <= 1: return 1
  return n * factorial(n-1)
print(factorial(5)) # 120

# 피보나치(for문)
def fibonacci(n):
  a, b = 1, 1
  if n==1 or n==2:
    return 1
  for i in range(1,n):
    a, b = b, a+b
  return a
print(fibonacci(1)) # 1
print(fibonacci(2)) # 1
print(fibonacci(3)) # 2
print(fibonacci(4)) # 3
print(fibonacci(5)) # 5
print(fibonacci(6)) # 8
print(fibonacci(7)) # 13

# 피보나치(재귀)
def fibonacci(n):
  if n <= 2: return 1
  return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(1)) # 1
print(fibonacci(2)) # 1
print(fibonacci(3)) # 2
print(fibonacci(4)) # 3
print(fibonacci(5)) # 5
print(fibonacci(6)) # 8
print(fibonacci(7)) # 13