import random
def binary_search(l, target):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

data = sorted(random.sample(range(1,30), 20))
target = random.randint(1,30)
print(f"data : {data}, target : {target}")
print(f"target index -> {binary_search(data, target)}")