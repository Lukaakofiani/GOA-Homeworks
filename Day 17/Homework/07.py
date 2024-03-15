def greater_then_10(numbers_greater_then_10):
  sum = 0
  for numbers in numbers_greater_then_10:
    if numbers >= 10:
      sum += numbers
    print(sum)
  

list = [6, 11, 30, 20, 1]

greater_then_10(list)
      