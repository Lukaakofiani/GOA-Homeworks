def remove_same_numbers(numbers):
  different_numbers = list(set(numbers))
  return different_numbers


new_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
print(remove_same_numbers(new_list))