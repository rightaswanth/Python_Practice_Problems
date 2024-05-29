# Python – Append Dictionary Keys and Values ( In order ) in dictionary

employe = {'id':1001, 'name':'john', 'place':'kochi'}

key_list = list(employe.keys())
value_list = list(employe.values())

employe_list = key_list + value_list

print(employe_list)