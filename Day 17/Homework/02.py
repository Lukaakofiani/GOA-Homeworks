def only_even_numbers(number_list):
  even_numbers = []
  for number in number_list:
    if number % 2 == 0:
      even_numbers.append(number)
    return(even_numbers)
  
input_even = [2, 7, 10, 20]
even_number = only_even_numbers(input_even)
print(even_number)