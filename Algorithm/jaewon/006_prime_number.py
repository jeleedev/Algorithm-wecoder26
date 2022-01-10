# O(N) 소수 구하기
import sys
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True
# 소수 입력  
n = int(sys.stdin.readline())
print(is_prime(n))

# O(sqrt(N)) 소수 구하기
import sys
from math import sqrt
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2,int(sqrt(n))+1):
    if n % i == 0:
      return False
  return True
# 소수 입력
n = int(sys.stdin.readline())
print(is_prime(n))

# O(N log log N) 소수 구하기
import sys
from math import sqrt
# eratosthenes_sieve
def eratosthenes_sieve(n):
  b = [True for i in range(n + 2) ] 
  b[1] = False 
  for i in range(2, int(sqrt(n)) + 1): 
    if b[i]:
      for j in range(i*i, n+1, i): 
        b[j] = False
  return b
# prime
def is_prime(b,n):
  return b[n]
# 1000까지의 수 중 소수를 구해둔 배열
b = eratosthenes_sieve(1000)
n = int(sys.stdin.readline())
print(is_prime(b,n))
