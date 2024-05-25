# Problem - 1
# Python program to interchange first and last elements in a list


# Method 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_element = numbers.pop(0)
last_element = numbers.pop(-1)

numbers.insert(0,last_element)
numbers.append(first_element)

print(numbers)


# Method 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = temp

print(numbers)


# Method 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[0] , numbers[-1] = numbers[-1] , numbers[0] 

print(numbers)



