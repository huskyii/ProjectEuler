def solve():
  return sum([x**2 for x in range(1,101)]) - sum(range(1,101)) ** 2

def quick_solve():
  return sum([x*y*2 for x in range(1,101) for y in range(x+1,101)])

if __name__ == "__main__":
  print solve()
  print quick_solve()
