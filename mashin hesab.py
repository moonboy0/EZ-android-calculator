from ctypes.wintypes import FLOAT
import math
from tkinter import N
from unittest import result
import math
z = int() 
x = z>=0
math.sqrt(x) 
try:
   num = float(input("enter first number:"))
except:
   print("invalid input pls try again")
try:
   num_2 = float(input("enter number:"))
except:
   print("invalid input pls try again")
try:
   op = str(input("word:"))
except:
   print("invalid input pls try again ")
if op == "+":
   result = num + num_2
elif op == "*":
   result = num * num_2
elif op == "/":
   result = num / num_2
elif op == "-":
   result = num - num_2
elif op == "**":
   result = num ** num_2
elif op == "sqrt":
   print(math.sqrt(num))
print(result)