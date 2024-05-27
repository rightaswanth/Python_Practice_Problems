# Python program to print even numbers in a list

# Method - 1

def even_numbers(numbers: list) -> list:
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = even_numbers(numbers)

print(result)

# Method - 2

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

even_list = list(filter(lambda x:x % 2 == 0, numbers))

print(even_list)

# Method - 3

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

even_list = [num for num in numbers if num % 2 == 0 ]

print(even_list)



