# Problem - 30
# Python – Closest Pair to Kth index element in Tuple

elements = (1, 4, 3, 8)
k = int(input("Enter the index of the element :"))
element = elements[k]
elements_list = list(elements)
elements_list.sort()
k = elements_list.index(element)
elements = tuple(elements_list)



if k == 0:
    pair = (elements[k+1],elements(k+2))
elif k == len(elements) - 1:
    pair = (elements[k-1],elements[k-2])
else:
    pair = (elements[k-1],elements[k+1])


print("Closest pair of the k th element in the tuple is : ",pair)