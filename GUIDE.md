# Guide til hvad vi gjore

Installer sympy
```
pip3 install sympy
```

Impoter sympy og alle de funktioner vi brugte
```
from sympy import *
```

Definer symboler så du kan bruge dem i koden
```
x, y, a, b, c, d = symbols('x y a b c d')
```

Sådan definerer du en ligning
```
# Samme som: 3x + 5x = 10
ligning = Eq(3*x + 5*x, 10)
```

Sådan definere du en funktion
```
# Samme som: f(x) = 10x
f = Eq(10*x)
```

Sådan indsætter du en x værdi i din funktion
```
# Samme som: f(5)
f.subs(x, 5)
# Giver 50
```

Sådan differentiere du en funktion
```
# Samme som: f'(x)
f_m = diff(f, x)

```
Sådan solver du noget
```
res = solve((ligning), (x))
```