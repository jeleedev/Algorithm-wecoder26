def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num in nums:
        s = s.replace(num, str(nums.index(num)))
    return int(s)
  
solution('one4seveneight')

'''
Python Dictionary

:: Key 추출
1. dic.keys()
2. for k in dic.keys() == for k in dic
3. key in dic ------> key가 있는지 확인 후 Ture or False 반환

:: Value 추출
1. dic.values()
2. dic[key]
3. dic.get(key)

:: Key & Value 추출
1. dic.items()
2. for k in dic.items() --------> tuple 형태로 반환
'''