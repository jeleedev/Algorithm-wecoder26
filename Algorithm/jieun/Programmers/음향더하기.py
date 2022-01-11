def solution(absolutes, signs):
    signs = [1 if sign else -1 for sign in signs]
    return sum([(signs[i] * absolutes[i]) for i in range(len(absolutes))])
  
solution([1,2,3], [False, False, True])