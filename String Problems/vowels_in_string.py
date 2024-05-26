# Problem - 20 
# Python program to accept the strings which contains all vowels

# Method - 1

vowels_small = "aeiou"
vowel_capital = "AEIOU"
fruit = "oraeiou"
flag = 0

for vowel_s,vowel_c in zip(vowels_small,vowel_capital): 
    # Using Zip for iterating the small and capital case of vowels same time
    if vowel_s not in fruit and vowel_c not in fruit:
        flag = 1
        break     # No need to continue the loop if the vowel not exist

if flag == 1:
    print("All vowels not present in the string ")
else:
    print("All vowels present in the string")

