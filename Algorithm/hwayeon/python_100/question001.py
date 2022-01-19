# 리스트의 삭제

# 다음 리스트에서 400, 500를 삭제하는 code를 입력하세요.
nums = [100, 200, 300, 400, 500]

# del 함수 사용
del nums[3:]

# remove() 사용
nums.remove(400)
nums.remove(500)

# pop() 사용
nums.pop()
nums.pop()

print(nums)