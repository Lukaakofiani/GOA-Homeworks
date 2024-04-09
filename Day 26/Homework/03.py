def func(manual_list):
  lst = []
  for elmn in manual_list:
    lst.append(len(str(elmn)))
  return lst.count(len(str(manual_list[-1])))


my_list = [1, 2, 2, 2, 4, 6, 8]
result = func(my_list)
print(result)