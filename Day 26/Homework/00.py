def func(manual_sum):
  lst = []
  sum = 0
  for num in manual_sum:
    sum += num
    lst.append(sum)
  return lst

lsst = [1, 2, 3, 4]
result = func(lsst)
print(result)