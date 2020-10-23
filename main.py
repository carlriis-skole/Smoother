from sympy import *
from utils import Errorhandling
from time import sleep
x, y, a, b, c, d = symbols('x y a b c d')
import math

while True:
      print("""
           _______..___  ___.   ______     ______   .___________. __    __   _______ .______      
          /       ||   \/   |  /  __  \   /  __  \  |           ||  |  |  | |   ____||   _  \     
         |   (----`|  \  /  | |  |  |  | |  |  |  | `---|  |----`|  |__|  | |  |__   |  |_)  |    
          \   \    |  |\/|  | |  |  |  | |  |  |  |     |  |     |   __   | |   __|  |      /     
      .----)   |   |  |  |  | |  `--'  | |  `--'  |     |  |     |  |  |  | |  |____ |  |\  \----.
      |_______/    |__|  |__|  \______/   \______/      |__|     |__|  |__| |_______|| _| `._____|
                                                                                            
      """)

      print("Vælg funktioner:")
      try:
            f1 = eval(input("f1: ").replace("^", "**"))
            f2 = eval(input("f2: ").replace("^", "**"))
      except SyntaxError or TypeError or NameError or ValueError or AttributeError:
            print("Error: One or both of your inputs, {} and {}, are invalid inputs".format(f1, f2))
            print("Hint: You need an x in all your functions. You can +x*0 if need be")
            sleep(3)
            break

      print("Vælg interval")
      in1 = input("i1: ")
      try:
            i1 = float(in1)
      except ValueError:
            Errorhandling.valerror(a)
            break
      
      in2 = input("i2: ")
      try:
            i2 = float(in2)
      except ValueError:
            Errorhandling.valerror(b)
            break

      try:
            eq1 = Eq(a*i1**3 + b*i1**2 + c*i1 + d, f1.subs(x, i1))

            eq2 = Eq(a*i2**3 + b*i2**2 + c*i2 + d, f2.subs(x, i2))

            eq3 = Eq(3*a*i1**2 + 2*b*i1 + c, diff(f1, x).subs(x, i1))

            eq4 = Eq(3*a*i2**2 + 2*b*i2 + c, diff(f2, x).subs(x, i2))

            sol = solve((eq1, eq2, eq3, eq4), (a, b, c, d))
      except SyntaxError or TypeError or NameError or ValueError or AttributeError:
            print("Error: One or both of your inputs, {} and {}, are invalid inputs".format(f1, f2))
            print("Hint: You need an x in all your functions. You can +x*0 if need be")
            sleep(3)
            break
            
      print("{}*x^3 + {}*x^2 + {}*x + {}".format(sol[a], sol[b], sol[c], sol[d]))
      
      slct = input("Do you want to continue?: ").lower()

      if slct == "no" or slct == "quit":
            break