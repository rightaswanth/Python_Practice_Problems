# Problem 11
# Python program to check if a string is palindrome or not

# Method - 1

my_wish = "malayalam"
new_wish = ""
length = len(my_wish)
i = 1 

while(i < length+1):
    new_wish += my_wish[-i]
    i = i + 1

if new_wish == my_wish:
    print("The string is palidrome")
else:
    print("The string is not palidrome")

# Method - 2
    
my_wish = "malayalam"
new_wish = my_wish[::-1]

if new_wish == my_wish:
    print("The string is palidrome")
else:
    print("The string is not palidrome")


