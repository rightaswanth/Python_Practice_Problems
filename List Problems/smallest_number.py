# Problem - 8
# Python program to find smallest number in a list

# Method - 1

numbers = [23, 12, 2, 56, 34]
small_number = numbers[0]

for num in numbers:
    if small_number > num:
        small_number = num

print("Smallest Number in Numbers list is :",small_number)

# Method - 2

numbers = [23, 12, 2, 56, 34]

numbers.sort()

print(f"Smallest number in numbers list is {numbers[0]}")

# Method - 3

numbers = [23, 12, 2, 56, 34]
smallest = numbers[0]
i = 0

while(i < len(numbers)):
    if smallest > numbers[i]:
        smallest = numbers[i]
    i += 1

print(f"Smallest number in this list is {smallest}")




