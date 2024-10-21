thing = input("Do you want addition, subtraction, multiplication, division, square root, or square? ")
import math
if thing == "addition":
  a = input("what is your first number? ")
  b = input("what is your second number? ")
  c = int(a) + int(b)
  print(str (c))
if thing == "subtraction":
  a = input("what is your first number? ")
  b = input("what is your second number? ")
  c = int(a) - int(b)
  print(str (c))
if thing == multiplication:
  a = input("what is your first number? ")
  b = input("what is your second number? ")
  c = int(a) * int(b)
  print(str (c))
if thing == division:
  a = input("what is your first number? ")
  b = input("what is your second number? ")
  c = int(a) / int(b)
  print(str (c))
if thing == "square root":
  a = input("What is the number? ")
  b = math.sqrt(a)
  print(str(b))
if thing == "square":
  a = input("What is the number? ")
  b = a ** 2
  print(str(b))
