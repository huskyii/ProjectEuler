# author  jiang
# email   mail.jiang.cn@gmail.com
# created on 2014-5-29

def solve():
  fib = [1,2]
  n = 2
  while fib[n-1] + fib[n-2] < 4000000:
    fib.append(fib[n-1] + fib[n-2])
    n += 1
  return sum(filter(lambda x: x if x%2 == 0 else 0, fib))

if __name__ == "__main__":
  print solve()
