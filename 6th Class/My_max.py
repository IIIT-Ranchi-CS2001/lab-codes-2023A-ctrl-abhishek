def my_max(data):
    if not isinstance(data, (list, set, tuple)):
        raise TypeError("Input must be a list, set, or tuple.")
    
    if isinstance(data, set):
        data = list(data)
    
    if len(data) == 0:
        raise ValueError("Cannot determine maximum of an empty data structure.")
    
    max_value = data[0]
    for item in data:
        if item > max_value:
            max_value = item
    return max_value

nums_list = [3, 5, 1, 9, 4]
print("Max in list:", my_max(nums_list))

nums_set = {3, 5, 1, 9, 4}
print("Max in set:", my_max(nums_set))

nums_tuple = (3, 5, 1, 9, 4)
print("Max in tuple:", my_max(nums_tuple))