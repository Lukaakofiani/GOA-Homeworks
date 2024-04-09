def func(manual_max):
  lst = []
  for numbers in manual_max:
    lst.append((numbers))
  return max((lst))
    
  
my_list = [1, 2, 3, 4, 5, 6]
result = func(my_list)
print(result)