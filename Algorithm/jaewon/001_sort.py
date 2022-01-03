import random

# bubble_sort
def bubble_sort(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap == False: break
    return data

# select_sort
def select_sort(data):
    for i in range(len(data)-1):
        lowest_idx = i
        for j in range(i+1, len(data)):
            if data[lowest_idx] > data[j]:
                lowest_idx = j
            data[lowest_idx], data[i] = data[i], data[lowest_idx]
    return data

# insert_sort
def insert_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else: break
    return data

# quick_sort
def quick_sort(data):
    if len(data) <= 1: return data
    pivot = data[0]
    left = [i for i in data[1:] if pivot > i]
    right = [i for i in data[1:] if pivot <= i]
    return quick_sort(left) + [pivot] + quick_sort(right)

# merge_sort
def merge_sort(data):
    if len(data) <= 1: return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    while left:
        merged.append(left.pop(0))
    while right:
        merged.append(right.pop(0))
    return merged



data_list = random.sample(range(100), 10)
print('bubble_sort :', bubble_sort(data_list))
print('select_sort :', select_sort(data_list))
print('insert_sort :', insert_sort(data_list))
print('quick_sort  :', quick_sort(data_list))
print('merge_sort  :', merge_sort(data_list))