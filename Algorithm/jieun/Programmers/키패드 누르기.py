keypad = [
  ['1','2','3'],
  ['4','5','6'],
  ['7','8','9'],
  ['*', '0', '#']
]


def solution(numbers, hand):
    left, right = (3,0), (3,2)
    answer = ''
    
    for num in numbers:
        num = str(num)
        location = [(x,y) for x in range(len(keypad)) for y in range(len(keypad[0])) if keypad[x][y] == num][0]
        
        if num in '147*':
            answer += 'L'
            left = location
        elif num in '369#':
            answer += 'R'
            right = location
        else:
          dl = abs(left[0] - location[0]) + abs(left[1] - location[1])
          dr = abs(right[0] - location[0]) + abs(right[1] - location[1])
          
          if dl == dr:
            answer += hand.upper()[0]
            if hand == 'left': left = location
            else: right = location
          elif dl < dr:
            answer += 'L'
            left = location
          else:
            answer += 'R'
            right = location
    return answer
  
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	, 'left')