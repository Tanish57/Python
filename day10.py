def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if(is_leap(year) == True and month == 2):
      output = 29
      return output
  else:
      output = month_days[month-1]
      return output
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#calculator

def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  '+': add ,
  '-': subtract, 
  '*':multiply, 
  '/': divide 
}
def calculator():
  flag = True
  num1 = int(input("What's the first number?: "))
  while flag != False:
    
    num2 = int(input("What's the second number?: "))
    
    print("Which operation do you want to perform of the following?")
    for symbol in operations:
      print(symbol)
    
    operator = input("Pick an operation from the line above: ")
    
    answer = operations[operator](num1, num2)
    
    print(f"{num1} {operator} {num2} = {answer}")
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to exit: ")
    if again == 'y':
      num1 = answer
    elif again == "exit":
      flag = False
    else:
      calculator()

calculator()