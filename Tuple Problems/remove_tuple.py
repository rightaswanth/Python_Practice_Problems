# Python – Remove Tuples of Length K

sequecnce = [(1,'name'), (1, 'appu'), (1, 2, 'hello'), (1, 2, 'funny', 4), (1, 2, 3, 'trick', 5)]

K = int(input("Enter the lenth of the tuple :"))

for value in sequecnce:
    size = 0
    t = tuple(value)
    if len(t) == K:
        ele_index = sequecnce.index(value)
        sequecnce.pop(ele_index)
        break

print(sequecnce)
