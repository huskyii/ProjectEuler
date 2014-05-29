# author  jiang
# email   mail.jiang.cn@gmail.com
# created on 2014-5-29

def solve():
  a = 600851475143
  while a != 1:
    b = 2
    while True:
      if a%b == 0:
        a = a/b
        lpf = b
        break
      else:
        b += 1
  return lpf

if __name__ == "__main__":
  print solve()
