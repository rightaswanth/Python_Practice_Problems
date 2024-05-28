# Python – Least Frequent Character in String

name = "hello world"
freeq_dict = {}

for n in name:
    counter = name.count(n)
    if n not in freeq_dict:
        freeq_dict[n] = counter

min_value = min([x for x in freeq_dict.values()])
min_ch_list = []

for key,value in freeq_dict.items():
    if freeq_dict[key] == min_value:
        min_ch_list.append(key)

print(min_ch_list)
 