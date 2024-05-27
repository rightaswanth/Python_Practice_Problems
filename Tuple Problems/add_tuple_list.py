# Problem - 29
# Python – Adding Tuple to List and vice – versa

# Adding tuple to list

prime_numbers = [2, 3, 5, 7, 11]
not_prime = (1, 4, 6, 8, 9)

# Coverting the tuple into list then add using + operation
all_numbers = prime_numbers + list(not_prime) 
 
print(all_numbers)

#Adding list to tuple

prime_numbers = [2, 3, 5, 7, 11]
not_prime = (1, 4, 6, 8, 9)

all_numbers = list(not_prime) + prime_numbers

all_numbers = tuple(all_numbers)

print(all_numbers)