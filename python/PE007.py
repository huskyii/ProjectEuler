# Sieve

def solve():
  res = xrange(2,110000)
  for i in xrange(10001):
    res = [x for x in res if x%res[i] != 0 or x == res[i] ]
  return res[10000]

if __name__ == "__main__":
  print solve()
