def solve():
  for i in xrange(333):
    for j in xrange(i,(1000-i)/2):
      k = 1000 - i - j
      if i**2 + j**2 == k**2:
        return i*j*k


if __name__ == '__main__':
  print solve()
