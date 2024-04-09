def func(manual_reduce):
  lst = []
  copied_list = []
  for item in manual_reduce:
    lst.append(item)
    copied_list.append(item)
  return lst, copied_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = func(my_list)
print(result)

  
