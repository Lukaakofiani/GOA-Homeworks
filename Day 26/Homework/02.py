def func(manual_min):
  lst = []
  for num in manual_min:
    lst.append((num))
  return min((lst))

my_list = [2, 4, 6, 8, 10]
result = func(my_list)
print(result)