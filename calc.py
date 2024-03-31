def main():
  print("This is very simple calculator. choose the calculation.")
  x = int(input("x > "))
  y = int(input("y > "))
  while(1):
    w = int(input("add: 1, substract: 2, multiply: 3, division: 4 >"))
    if w == 1:
      print("%d + %d = %d" % (x, y, add(x,y)))
      break
    elif w == 2:
      print("%d - %d = %d" % (x, y, substract(x,y)))
      break
    elif w==3:
      print("%d * %d = %d" % (x, y, multiply(x,y)))
      break
    elif w==4:
      print("%d / %d = %0.3f" % (x, y, divide(x,y)))
      break
    else:
      print("Wrong answer. Let's choose correct operator")
    
    
def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(x, y):
  return  x * y

def divide(x, y):
  if y == 0:
    print("Error: cannot divide by zero.")    
  else:
    return x / y    

if __name__ == "__main__":
  main()
