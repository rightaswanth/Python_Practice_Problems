# Python program to print odd numbers in a List

# Method - 1

def odd_numbers(numbers: list) -> list:
    odd_list = []
    for num in numbers:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
result = odd_numbers(numbers)

print(result)

# Method - 2

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

odd_list = list(filter(lambda x:x % 2 != 0, numbers))

print(odd_list)

# Method - 3

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

odd_list = [num for num in numbers if num % 2 != 0 ]

print(odd_list)
