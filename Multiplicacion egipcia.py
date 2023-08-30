'''Teoría computacional Algoritmos: Multiplicación egipcia'''

a = int(input())
b = int(input())
if a < b:
  c = a
  a = b
  b = c
mult = 1
while mult < b:
  mult *= 2
if mult == b:
  result = a * b
else:
  mult /= 2
  result = a * mult
  n = mult
  mult /= 2
  while mult >= 1:
    if n + mult <= b:
      result += a * mult
      n += mult
    mult /= 2
print(result)