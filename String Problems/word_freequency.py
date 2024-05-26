# Problem - 16 
# Python – Words Frequency in String Shorthands

# Method - 1

my_wish = "hello abi and hello aisha"
wish_list = my_wish.split(" ")
frequency_count = {}

for wish in wish_list:
    if wish not in frequency_count:
        frequency_count[wish] = wish_list.count(wish)
        
print(frequency_count)
