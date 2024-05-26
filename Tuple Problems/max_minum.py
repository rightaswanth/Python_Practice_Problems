# Problem - 27
# Python – Maximum and Minimum K elements in Tuple

scores = (23, 45, 67, 89, 34)
k = int(input("Enter the value of K :"))

scores_list = list(scores)
scores_list.sort()
scores = tuple(scores_list)

print("Maximum K element is :",scores[-k:])
print("Minimum K element is :",scores[:k])
