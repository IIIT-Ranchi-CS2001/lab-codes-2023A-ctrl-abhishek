def my_sort(data, key=0):
    if key < 0 or key >= len(data[0]):
        raise ValueError(f"Invalid key: {key}. Must be 0, 1, or 2.")
    
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103]
shopping_points = [120, 90, 150]

data = my_zip(True, customer_name, customer_id, shopping_points)
print("Original Data:", data)

sorted_by_name = my_sort(data, key=0)
print("Sorted by Name:", sorted_by_name)

sorted_by_id = my_sort(data, key=1)
print("Sorted by ID:", sorted_by_id)

sorted_by_points = my_sort(data, key=2)
print("Sorted by Shopping Points:", sorted_by_points)