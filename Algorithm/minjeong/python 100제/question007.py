# 문제7 : 변수명

# 다음 중 변수명으로 사용할 수 없는 것 2개를 고르시오.

# 1)  age
# 2)  a
# 3)  as
# 4)  _age
# 5)  1age

# 답 3, 5번

# 3번: python keyword는 사용할 수 없다. 
# 5번: 숫자로 시작할 수 없다.

# 변수명 생성 규칙
# - 영문 문자와 숫자를 사용할 수 있다.
# - 대소문자를 구분한다.
# - 문자부터 시작해야 하며 숫자부터 시작하면 안된다.
# - _(밑줄 문자)로 시작할 수 있다.
# - 특수 문자(+, -, *, /, $, @, &, %등)는 사용할 수 없다.

import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'break', \
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', \
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', \
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', \
    'try', 'while', 'with', 'yield']