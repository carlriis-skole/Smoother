from sympy import symbols, Eq, solve, diff

while True:
      print("""
           _______..___  ___.   ______     ______   .___________. __    __   _______ .______      
          /       ||   \/   |  /  __  \   /  __  \  |           ||  |  |  | |   ____||   _  \     
         |   (----`|  \  /  | |  |  |  | |  |  |  | `---|  |----`|  |__|  | |  |__   |  |_)  |    
          \   \    |  |\/|  | |  |  |  | |  |  |  |     |  |     |   __   | |   __|  |      /     
      .----)   |   |  |  |  | |  `--'  | |  `--'  |     |  |     |  |  |  | |  |____ |  |\  \----.
      |_______/    |__|  |__|  \______/   \______/      |__|     |__|  |__| |_______|| _| `._____|
                                                                                            
      """)

      x, y, a, b, c, d = symbols('x y a b c d')


      print("Vælg funktioner:")
      f1 = eval(input("f1: ").replace("^", "**"))
      f2 = eval(input("f2: ").replace("^", "**"))

      print("Vælg interval")
      i1 = int(input("i1: "))
      i2 = int(input("i2: "))

      eq1 = Eq(a*i1**3 + b*i1**2 + c*i1 + d, f1.subs(x, i1))

      eq2 = Eq(a*i2**3 + b*i2**2 + c*i2 + d, f2.subs(x, i2))

      eq3 = Eq(3*a*i1**2 + 2*b*i1 + c, diff(f1, x).subs(x, i1))

      eq4 = Eq(3*a*i2**2 + 2*b*i2 + c, diff(f2, x).subs(x, i2))

      sol = solve((eq1, eq2, eq3, eq4), (a, b, c, d))

      print("{}*x^3 + {}*x^2 + {}*x + {}".format(sol[a], sol[b], sol[c], sol[d]))
      
      slct = input("Do you want to continue?: ").lower()

      if slct == "no" or slct == "quit":
            break