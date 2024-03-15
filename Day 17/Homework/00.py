def sum_of_all_numbers(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum

input_list = [1, 6, 9, 10]
other_list = sum_of_all_numbers(input_list)
print(other_list)
