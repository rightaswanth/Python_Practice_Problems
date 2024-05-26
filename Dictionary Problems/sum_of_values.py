# Problem - 22
# Python program to find the sum of all items in a dictionary

# Method - 1

scores = {'abi':22, 'aks':25, 'nj':34, 'asw':28}
score_sum = 0

for score in scores.values():
    score_sum += score

print("Sum of all values is ",score_sum)


