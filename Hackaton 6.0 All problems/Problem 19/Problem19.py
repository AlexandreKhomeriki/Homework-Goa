def manual_min(lst):
    if not lst:  
        return None

    min_value = lst[0]  
    for num in lst:
        if num < min_value:  
            min_value = num  
    return min_value


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(manual_min(numbers))  
