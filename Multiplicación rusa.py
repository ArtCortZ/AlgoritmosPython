'''Teoría computacional Algoritmos: Multiplicación rusa'''

a = int(input())
b = int(input())
result = 0
while a >= 1:
  if a%2 != 0:
    result += b
    a -= 1
  a /= 2
  b *= 2
print(result)