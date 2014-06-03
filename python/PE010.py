# Sieve

sieve = [True]*2000000

def mark(sieve,x):
  for i in xrange(x+x,len(sieve),x):
    sieve[i] = False

def solve():
  for x in xrange(2,int(len(sieve)**0.5) + 1):
    if sieve[x]:
      mark(sieve,x)
  return sum(i for i in xrange(2,len(sieve)) if sieve[i])

if __name__ == "__main__":
  print solve()
