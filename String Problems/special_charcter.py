# Python | Program to check if a string contains any special character

def check_special_character(password: str):
    flag = 0
    for ch in password:
        if ch.isdigit() or ch.isalpha():
            continue
        else:
            flag = 1
            break
    return flag

password = "aswgmailcom"
result = check_special_character(password)
if result == 1:
    print("The special Character is finded")
else:
    print("The string not contain the special character")



