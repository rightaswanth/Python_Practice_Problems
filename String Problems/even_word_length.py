# Problem - 19
# Python program to print even length words in a string

# Method - 1

my_wish = "Hello i am tomy"
wish_list = my_wish.split(" ")

for wish in wish_list:
    if len(wish) % 2 == 0:
        print(wish)