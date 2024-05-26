# Problem - 14
# Ways to remove i’th character from string in Python

# Method - 1

my_name = "Aswanth"
ch_index = int(input("Enter the character index  for removing:"))

my_name=my_name.replace(my_name[ch_index]," ")

print(my_name)