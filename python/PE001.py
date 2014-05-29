# author  jiang
# email   mail.jiang.cn@gmail.com
# created on 2014-5-28

def solve():
  s = set()
  i = 1
  while i*3 < 1000:
    s.add(3*i)
    if 5 * i < 1000: 
      s.add(5*i)
    i += 1
  return sum(s)

if __name__ == "__main__":
  print solve()
