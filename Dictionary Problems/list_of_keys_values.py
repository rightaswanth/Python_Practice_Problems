# Python – Sort Dictionary key and values List

student = {'name': 12, 'age': 23 , 'class': 10, 'place': 30, 'mark': 86}

values_list = [x for x in student.values()]
keys_list = [x for x in student.keys()]

while True:
    try:
        values_list.sort()
        keys_list.sort()
        print(values_list)
        print(keys_list)
        break
    except TypeError:
        print("The key and value list is not homogenous , So sorting is not possible")
        break


