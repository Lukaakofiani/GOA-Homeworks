def func(first_character):
  return [s for s in first_character if s.startswith("a")]
  
input_list = ["apple", "avocado", "orange"]
other_list = func(input_list)
print(other_list)