# Problem - 7
# Python program to find sum of elements in list

# Method - 1

numbers = [2, 4, 5, 78, 23, 34]
sum_of_elemnts = 0

for num in numbers:
    sum_of_elemnts += num

print(sum_of_elemnts)

# Method - 2

numbers = [2, 4, 5, 78, 23, 34]
sum_of_elemnts = 0
i = 0

while(i < len(numbers)):
    sum_of_elemnts += numbers[i]
    i += 1

print(sum_of_elemnts)

# Method - 3

numbers = [2, 4, 5, 78, 23, 34]

sum_of_elemnts = sum(numbers)

print(sum_of_elemnts)




