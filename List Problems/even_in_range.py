# Python program to print all even numbers in a range

# Method - 1

start = int(input("Enter the input of statring the range :"))
end = int(input("Enter the input of ending the range :"))
# The start and end variables for specifying the range 
# For filter the even list

even_list = [x for x in range(start, end) if x % 2 == 0]
# Using list comprehesion method for creating even elements list

print(even_list)

# Method - 2

start = int(input("Enter the input of statring the range :"))
end = int(input("Enter the input of ending the range :"))

even_list = list(filter(lambda x : x % 2 == 0, range(start, end)))
# Using lambda function and filter list method 

print(even_list)



