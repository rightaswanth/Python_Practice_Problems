# Python | Maximum frequency character in String


name = "hello world"
freeq_dict = {}

for n in name:
    counter = name.count(n)
    if n not in freeq_dict:
        freeq_dict[n] = counter

max_value = max([x for x in freeq_dict.values()])
max_ch_list = []

for key,value in freeq_dict.items():
    if freeq_dict[key] == max_value:
        max_ch_list.append(key)

print(max_ch_list)
 