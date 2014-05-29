def get_prime_factors(a):
  factors = []
  counts = []
  while a != 1:
    b = 2
    while True:
      if a%b == 0:
        a /= b
        if b not in factors:
          factors.append(b)
          counts.append(1)
        else:
          counts[factors.index(b)] += 1
        break
      else:
        b += 1
  return zip(factors,counts)

def solve():
  factors_with_counts = []
  factors = []
  res = 1
  for i in range(2,21):
    factors_with_counts += get_prime_factors(i)
  factors += map(lambda x: x[0],factors_with_counts)
  factors_set = set(factors)
  for factor in factors_set:
    max_tuple = max([x for x in factors_with_counts if x[0] == factor],key = lambda x: x[1])
    res *= max_tuple[0] ** max_tuple[1]
  return res

if __name__ == '__main__':
  print solve()
