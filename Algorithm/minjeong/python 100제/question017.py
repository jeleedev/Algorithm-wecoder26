# 문제17 : 놀이기구 키 제한

# 유주는 놀이공원 아르바이트 중입니다. 그런데 놀이기구마다 키 제한이 있습니다.
# 유주가 담당하는 놀이기구는 키가 150 이상만 탈 수 있습니다.

# 입력으로 키가 주어지면
# 키가 150이 이상이면 YES를 틀리면 NO를 출력하는 프로그램을 작성하세요.

tall = int(input())

if tall >= 150:
    print('YES')
else:
    print('NO')
    
# 답안

n = int(input())
if n < 150:
	print("NO")
elif 150 <= n:
	print("YES")