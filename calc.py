thing = input("Do you want addition, subtraction, multiplication, division, square root, square, cube, or cube root? ")
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
if thing == "multiplication":
  a = input("what is your first number? ")
  b = input("what is your second number? ")
  c = int(a) * int(b)
  print(str (c))
if thing == "division":
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
if thing == "cube":
  a = input("What is the number? ")
  b = a ** 3
  print(str(b))
if thing == "cube root":
  a = input("What is the number? ")
  b = a ** (1/3)
  print(str(b))
