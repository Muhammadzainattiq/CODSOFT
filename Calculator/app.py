def calculator(a:int,b:int,operator:str)->int:
  if operator == "+":
    return a+b
  elif operator == "-":
    return a-b

  elif operator == "*":
    return a*b

  elif operator == "/":
    if b!=0:
      return a/b
    else:
      return "Division by zero is not allowed"
  else:
    return "Invalid operator"
while True:
  a = int(input("Enter the first number:"))
  b = int(input("Enter the second number:"))
  operator = input("Enter the operator:")
  result = calculator(a,b,operator)
  print(result)