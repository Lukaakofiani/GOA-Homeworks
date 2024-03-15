def largest(numbers):
    if not numbers:
        return None  
    max_num = numbers[0]  
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


numbers = [2, 67, 90, 3]
print("The largest list number is", largest(numbers))