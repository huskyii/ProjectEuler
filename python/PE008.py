def product(lst):
  res = 1
  for elem in lst:
    res *= elem
  return res

def max_product(lst):
  lst = [int(x) for x in lst]
  if len(lst) == 13:
    return product(lst)
  products = [product(lst[i:i+13]) for i in range(len(lst) - 12) ]
  return max(products)


def solve():
  nums = ''
  with open('PE008.txt','r') as file:
    for line in file:
      line = line.strip()
      nums += line
  nums = nums.split('0')
  max_products = [max_product(list(num)) for num in nums if len(num) >= 13]
  return max(max_products)

if __name__ == '__main__':
  print solve()
