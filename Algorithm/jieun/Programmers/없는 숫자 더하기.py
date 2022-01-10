def solution(numbers):
    # answer = 0
    # numbers.sort()
    # for i in range(10):
    #     if not i in numbers: answer += i          
    # return answer
  
    return sum(range(10)) - sum(numbers)
  
solution([1,2,3,4,6,7,8,0])