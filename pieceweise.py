
from sympy import *
x, y, a, b, c, d = symbols('x y a b c d')

print("""
 _______  __   __  _______  _______  _______  __   __  _______  ______   
|       ||  |_|  ||       ||       ||       ||  | |  ||       ||    _ |  
|  _____||       ||   _   ||   _   ||_     _||  |_|  ||    ___||   | ||  
| |_____ |       ||  | |  ||  | |  |  |   |  |       ||   |___ |   |_||_ 
|_____  ||       ||  |_|  ||  |_|  |  |   |  |       ||    ___||    __  |
 _____| || ||_|| ||       ||       |  |   |  |   _   ||   |___ |   |  | |
|_______||_|   |_||_______||_______|  |___|  |__| |__||_______||___|  |_|

---------------------------------
       Pieceweise edition
---------------------------------

""")

print("Funktion:")
funk = input()

sætninger = ((funk.split("piecewise(")[1].replace(")", "").split(",")))

inta = 0.6

funks = []

rans = []

for i in range(0, int((len(sætninger)+1)/float(2))):
    funks.append(eval((sætninger[i*2 + 1] + " + 0*x").replace("^", "**")))

    ran = sætninger[i*2].strip(" ")
    rans.append(float(ran.split(" ")[0]))


last_i = 0
product = "piecewise("

ran = sætninger[len(sætninger)-2].split(" ")
rans.append(float(ran[len(ran)-1]))

last_rand = 0
lenghts = []
for i in range(0, len(rans)-1):
    lenghts.append(rans[i+1]-last_rand)
    last_rand=rans[i+1]


ranges = [rans[0]]

total = 0
for i in range(0, len(lenghts)):
    if (i != len(lenghts)-1):
        ranges.append(lenghts[i]*inta + total)
    total += lenghts[i]*inta
    ranges.append(lenghts[i]*(1-inta) + total)
    total += lenghts[i]*(1-inta)


for i in range(0, len(ranges)-1):
    i1 = ranges[i]
    i2 = ranges[i+1]

    if i % 2 == 0:
        funk = funks[int(i/2)]
        product += str(i1) + " < x < " + str(i2) + ", " + str(funk) + ", "
    else:
        f1 = funks[int((i-1)/2)]
        f2 = funks[int((i+1)/2)]


        eq1 = Eq(a*i1**3 + b*i1**2 + c*i1 + d, f1.subs(x, i1))
        eq2 = Eq(a*i2**3 + b*i2**2 + c*i2 + d, f2.subs(x, i2))
        eq3 = Eq(3*a*i1**2 + 2*b*i1 + c, diff(f1, x).subs(x, i1))
        eq4 = Eq(3*a*i2**2 + 2*b*i2 + c, diff(f2, x).subs(x, i2))
        sol = solve((eq1, eq2, eq3, eq4), (a, b, c, d))

        res = ("{}*x^3 + {}*x^2 + {}*x + {}".format(sol[a], sol[b], sol[c], sol[d]))

        product += str(i1) + " < x < " + str(i2) + ", " + str(res) + ", "


product = list(product)

product[len(product)-2] = ")"
product = "".join(product)

print()
print(product)