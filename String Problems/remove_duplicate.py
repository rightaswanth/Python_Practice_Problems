# Remove all duplicates from a given string in Python

my_name = "aswanth"
my_name = my_name.upper()
unique_list =[]

for name in my_name:
    if name not in unique_list:
        unique_list.append(name)

my_name = "".join(unique_list)
my_name = my_name.title()

print(my_name)
print(unique_list)

