# 문제21 : set은 어떻게 만드나요?

# 다음 중 set을 만드는 방법이 아닌 것?

# 1)  x = {1, 2, 3, 5, 6, 7}
# 2)  x = {}
# 3)  x = set('python')
# 4)  x = set(range(5))
# 5)  x = set()

# 답 2번


a = {1, 2, 3, 5, 6, 7}
b = {}
c = set('python')
d = set(range(5))
e = set()

print(type(a)) # set
print(type(b)) # dict
print(type(c)) # set
print(type(d)) # set
print(type(e)) # set