# 문제1 : 리스트의 삭제
# 다음 리스트에서 400, 500를 삭제하는 code를 입력하세요.

# remove 사용
nums1 = [100, 200, 300, 400, 500]

nums1.remove(400)
nums1.remove(500)

print(nums1)

# del 사용
nums2 = [100, 200, 300, 400, 500]

del nums2[3:5]

print(nums2)

# pop() 사용

nums3 = [100, 200, 300, 400, 500]

nums3.pop(3)
nums3.pop()

print(nums3)


# 답안
nums = [100, 200, 300, 400, 500]
nums.pop()
nums.pop()
print(nums)