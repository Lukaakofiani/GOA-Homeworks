def filter(collection, value):
  lst = []
  for item in collection:
    if item == value:
      lst.append(item)
  return lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
filtered = filter(my_list, my_list1)
print(filtered)