customer_names = [f"Customer{i}" for i in range(1, 6)]
customer_ids = [1000 + i for i in range(1, 6)]
shopping_points = [10 * i for i in range(1, 6)]

customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

sorted_with_function = sorted(customer_data_zip, key=lambda x: x[1])

sorted_without_function = customer_data_zip[:]  
for i in range(len(sorted_without_function)):
    for j in range(len(sorted_without_function) - i - 1):
        if sorted_without_function[j][1] > sorted_without_function[j + 1][1]:
            sorted_without_function[j], sorted_without_function[j + 1] = sorted_without_function[j + 1], sorted_without_function[j]

print("Sorted using sorted():", sorted_with_function)
print("Sorted without using sorted():", sorted_without_function)
