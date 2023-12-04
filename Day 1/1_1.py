import sys


sum_of_digits = 0

filename = sys.argv[1]+".txt"

with open(filename, "r") as file:
    lines = [line.rstrip("\n") for line in file]

for string in lines:
    first_digit = ''
    last_digit = ''
    for char in string:
        if char.isdigit():
            if first_digit == '':
                first_digit = char
            last_digit = char
        #combine the two digit in a number
    concat=first_digit+last_digit
    sum_of_digits += int(concat)



print(sum_of_digits)



