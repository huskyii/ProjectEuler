def is_palindrome(s):
  front,back = 0, len(s) -1
  while front < back:
    if s[front] != s[back]:
      return False
    front += 1
    back -= 1
  return True

def solve():
  tmp = [(x,y) for x in range(100,1000) for y in range(100,1000)]
  products = [x[0] * x[1] for x in tmp]
  return max([x for x in products if is_palindrome(str(x))])

if __name__ == '__main__':
  print solve()
