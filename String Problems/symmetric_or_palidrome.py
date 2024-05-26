# Problem - 12
# Python program to check whether the string is Symmetrical or Palindrome

check_string = "malayalam"
new_symetric = ""
new_palidrome = check_string[::-1]

half_index = len(check_string) // 2

if check_string[:half_index] == check_string[half_index:]:
    print("The string is symmeteric ")
elif new_palidrome == check_string and check_string[:half_index] == check_string[half_index:]:
    print("The string is palindrome and symmetric")
elif new_palidrome == check_string:
    print("The string is  palindrome")
else:
    print("The string is not palidrome and not symmetrical")
