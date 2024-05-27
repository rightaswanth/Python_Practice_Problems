# Python program to find N largest elements from a list


def largest_elements(n: int, numbers: list) -> list:
    numbers.sort()
    larg_elements = numbers[-n:]
    return larg_elements

numbers = [34,23,98,12,56,78]
N = int(input("Enter the value of N :"))
result = largest_elements(N,numbers)

print("N largest elements in the list are :",result)


