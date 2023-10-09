from re import X
import string


def math_expr(expr: str) -> bool:
    if '+' in expr:
        y = expr.split('+')
        x = int(y[0])+int(y[1])
        return True
   
    if '-' in expr:
      y = expr.split('-')
      x = int(y[0])-int(y[1])
      return True

    if '*' in expr:
      y = expr.split('*')
      x= int (y[0])*int(y[1])
      return True
    
    if '/' in expr:
      y = expr.split('/')
      x= int (y[0])/int(y[1])
      return True
    

print(math_expr('3-3'))
