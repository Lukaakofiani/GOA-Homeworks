def func(square_numbers):
  squarenum_list = []
  for num in square_numbers:
    squarenum_list.append(num ** 2)
  return squarenum_list

input_list = [12, 89, 32, 90]
squared_numbers = func(input_list)
print(squared_numbers)