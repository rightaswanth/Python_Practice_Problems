# Problem - 17
# Python – Convert Snake case to Pascal case

# Method - 1

snake_case = "hello_world"
pascal_case = snake_case.title()
pascal_case = pascal_case.replace('_',"")
print(pascal_case)