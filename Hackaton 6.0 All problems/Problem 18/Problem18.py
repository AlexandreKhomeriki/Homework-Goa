def manual_min(numbers):
    if not numbers:
        raise ValueError("List is empty")

    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(manual_min(example_list))  
