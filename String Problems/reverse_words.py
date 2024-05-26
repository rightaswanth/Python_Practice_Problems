# Problem - 13
# Reverse words in a given String in Python

my_wish = "Hello world"
wish_list = my_wish.split(" ")
reversed_list = []

for i in range(len(wish_list)-1,-1,-1):
    reversed_list.append(wish_list[i])

reversed_string = " ".join(reversed_list)

print(reversed_string)
