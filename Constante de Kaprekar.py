'''Teoría computacional Algoritmos: Constante de kaprekar'''

def order_digits(num_str, reverse=False):
  sorted_str = ''.join(sorted(num_str))
  if reverse:
    sorted_str = sorted_str[::-1]
  return int(sorted_str)


def kaprekar_constant(n):
  count = 0
  while n != 6174:
    ascending = order_digits(str(n))
    descending = order_digits(str(n), reverse=True)
    n = descending - ascending
    count += 1
    print(f"Iteration {count}: {descending} - {ascending} = {n:04d}")
  return count

initial_number = int(input())
iterations = kaprekar_constant(initial_number)
print(f"Se alcanzó la constante de Kaprekar en {iterations} iteraciones.")
