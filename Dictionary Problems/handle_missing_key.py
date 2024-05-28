# Handling missing keys in Python dictionaries

student = {'name': 'Abi', 'age': 23 , 'class': 10, 'place': 'calicut', 'mark': 86}


while True:
    try:
        key_name = input("Enter the key of the dictionary :")
        print(student[key_name])
    except KeyError:
        print('You entered a wrong key')
        break


