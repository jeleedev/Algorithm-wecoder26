# 2-gram

# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다. 
# 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.

# Py
# yt
# th
# ho
# on

# 입력으로 문자열이 주어지면 2-gram으로 출력하는 프로그램을 작성해 주세요.

# 답안
str = input()
for i in range(len(str)-1):
    print(str[i], str[i+1], sep='')
