def isValid(s: str) -> bool:
  s_splited = []
  for char in s:
    if char in '([{':
      s_splited.append(char)
      print(s_splited)
    else:
      if not s_splited or \
        (char == ')' and s_splited[-1] != '(') or \
        (char == ']' and s_splited[-1] != '[') or \
        (char == '}' and s_splited[-1] != '{'):
          return False
      s_splited.pop()
  return not s_splited      
             
s = ""

print(isValid(s))