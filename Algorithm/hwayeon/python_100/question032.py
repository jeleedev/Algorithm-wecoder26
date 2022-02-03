# 문자열 만들기
# 취업 준비생인 혜림이는 자기소개서를 쓰고 있습니다. 열심히 자기소개서를 작성하던 도중 혜림이는 자기가 지금까지 단어를 얼마나 적었는지 궁금하게 됩니다. 

# 혜림이를 위해 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해 주세요.

# 입력 : 안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다.
# 출력 : 5

n = input()
result = n.strip().split()
print(len(result))

# strip() : 문자열 앞뒤의 공백 또는 특별한 문자 삭제.
text = ' Water boils at 100 degrees '
print('[' + text.rstrip() + ']')
# [ Water boils at 100 degrees]

print('[' + text.lstrip() + ']')
# [Water boils at 100 degrees ]

print('[' + text.strip() + ']')
# [Water boils at 100 degrees]

# split() : 문자열 내부에 있는 공백 또는 특별한 문자를 구분해서 리스트로 만듦.