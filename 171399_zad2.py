def eval_expression(operator, value_one, value_two):
  if operator == "+":
    return float(value_one + value_two)
  elif operator == "-":
    return value_one - value_two
  elif operator == "*":
    return value_one * value_two
  elif operator == "/":
    return value_one / value_two
  else:
      print ("Zly operator: " + operator)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def main():
  while True:
    eval_stack = [ ]
    
    line = input('> ')
    tokens = line.rstrip().split(' ')
    
    if len(tokens) <= 2:
      if line == 'q':
        break
      print ('Blad! - wpisz operator oraz conajmniej dwa elementy na ktorych chcesz wykonac operacje')
      continue
       
    for token in tokens:
      if is_number(token.replace(',', '.')):
        token = float(token)
        eval_stack.append(token)
        
        if len(eval_stack) >2:  
          second = eval_stack.pop()
          first = eval_stack.pop()
          eval_stack.append(eval_expression(eval_stack[0], first, second))
      else:
        if len(eval_stack) != 0:
          eval_stack[0] = token
        else:   
          eval_stack.insert(0, token)

    print (eval_stack[-1])

if __name__ == '__main__':
  main()
