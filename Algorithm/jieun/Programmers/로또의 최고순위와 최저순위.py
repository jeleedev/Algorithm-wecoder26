def solution(lottos, win_nums):
    answer = []
    zero = len([num for num in lottos if num == 0])
    intersection = list(set(lottos) & set(win_nums))
    
    min = len(intersection)
    max = zero + min 
    
    answer = [7-max if max > 0 else 6, 7-min if min > 1 else 6]
    return answer
  

''' ---------- TEST CASE ---------- 
# 기본 케이스
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

# 로또번호가 모두 가려졌을 때
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

# 로또번호가 모두 일치할 때
lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

# 로또번호가 하나도 일치하지 않을 때
lottos = [1,2,3,4,5,6]
win_nums = [7,8,9,10,11,12]
'''