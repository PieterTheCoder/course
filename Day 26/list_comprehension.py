# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_name = [name.upper() for name in names if len(name) > 5]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number * number for number in numbers]
# print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)
