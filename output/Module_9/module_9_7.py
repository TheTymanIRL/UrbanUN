def is_prime(func):
  def wrapper(*args):
    summ = func(*args)
    del_ = 0
    for i in range(summ+1):
      if i != 0:
        if summ % i == 0:
          del_ += 1
    if del_ <= 2:
      print('Простое')
      return summ
    else:
      print('Составное')
      return summ
  return wrapper

@is_prime
def sum_three(a, b, c):
  return a + b + c
  
result = sum_three(2, 3, 6)
print(result)
