def multiple_of_4(numbers):
  filtered = [num for num in numbers if num % 4 == 0]
  return filtered


numbers_from_1_to_20 = (range(1, 21))
print(multiple_of_4(numbers_from_1_to_20))