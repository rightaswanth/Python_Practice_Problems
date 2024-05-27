# Python | Count the Number of matching characters in a pair of string


def match_counter(fruit_one: str, fruit_two: str) -> list:
    conuter_list = []
    for one in fruit_one:
        for two in fruit_two:
            if one == two:
                if one not in conuter_list:
                    conuter_list.append(one)
    return conuter_list

fruit_first = "apple"
fruit_second = "orange"

result = match_counter(fruit_first,fruit_second)
print("Number of matching character in pair of string :",len(result))

