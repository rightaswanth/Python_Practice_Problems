# Problem - 2
# Python program to swap two elements in a list

# Method 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

element_one = int(input("Enter the first element for swapping :"))
element_two = int(input("Enter the second element for swapping :"))

index_one = numbers.index(element_one)
index_two = numbers.index(element_two)

temp = numbers[index_one]
numbers[index_one] = numbers[index_two]
numbers[index_two] = temp

print(numbers)


# Method 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

element_one = int(input("Enter the first element for swapping :"))
element_two = int(input("Enter the second element for swapping :"))

index_one = numbers.index(element_one)
index_two = numbers.index(element_two)

numbers[index_one] , numbers[index_two] = numbers[index_two] , numbers[index_one]

print(numbers)





