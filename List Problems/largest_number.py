# Problem - 10
# Python program to find largest number in a list

# Method - 1

numbers = [12, 34, 5, 56, 1]
largest_number = numbers[0]

for num in numbers:
    if largest_number < num:
        largest_number = num

print("The Largest number in this list is ",largest_number)

# Method - 2

numbers = [12, 34, 5, 56, 1]

numbers.sort()

largest_number = numbers[-1]

print(f"Largest number in numbers list is ",largest_number)




