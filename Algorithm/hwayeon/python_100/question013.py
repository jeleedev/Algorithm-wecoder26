# 몇 번째 행성인가요?

# 우리 태양계를 이루고 있는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성으로 총 8개 입니다.
# 저희는 우리 태양계의 n번째 행성이 무엇인지 알고 싶습니다.
# 입력으로 행성의 순서를 나타내는 숫자 n이 입력됩니다. 예를 들어 수성은 첫번째 행성입니다.
n = 1

# 출력으로 그 순서에 해당하는 행성의 이름을 출력해 주세요.

# 답안
planets = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

num = int(input())-1
print(planets[num])

# 답안 2
planets = {1:'수성', 2:'금성', 3:'지구', 4:'화성', 5:'목성', 6:'토성', 7:'천왕성', 8:'해왕성'}

num = int(input())
print(planets[num])