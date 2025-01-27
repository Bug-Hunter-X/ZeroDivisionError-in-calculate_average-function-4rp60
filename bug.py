def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Example
my_numbers = [10,20,30,40,50]
avg = calculate_average(my_numbers)
print(avg)