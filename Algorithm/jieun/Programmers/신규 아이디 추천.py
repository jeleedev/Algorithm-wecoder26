import re

def solution(new_id):
    str = new_id.lower()
    
    str = ''.join(re.findall('[a-z0-9_.-]', str))
    
    for _ in range(len(str)):
      str = str.replace('..', '.')
      
    str = removeDot(str)
    
    str = str if str != '' else 'a'
    
    str = str[:15] if len(str) >= 16 else str 
    str = removeDot(str)
    
    while len(str) <= 2:
      str = str + str[-1]
      
    return str

def removeDot(str):
  if len(str) < 1: return str

  str = str[1:] if str[0] == '.' else str
  str = str[:-1] if len(str) >= 1 and str[-1] == '.' else str
  return str  

solution('123_.def')

'''
💡️ 정규식만으로 풀었을 때 답안

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''