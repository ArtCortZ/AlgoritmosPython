'''Teoría computacional Algoritmos: Conjetura de Collatz'''

#Conjetura de Collatz
n = int(input())
while n > 1:
  if n % 2 == 0:
    n /= 2
  else:
    n = (3 * n) + 1
  print(n)
