def width_length(numbers):
  total_numbers = sum(numbers)

  mean =  total_numbers / len(numbers)

  return mean


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(width_length(numbers))