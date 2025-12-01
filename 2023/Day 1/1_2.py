import sys
import re

digit_mapping = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def find_digit_spelled_with_letters(string,n):
    digit_pattern = r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)'
    digit_pattern2 = r'(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)'
    
    if n==1:
        match = re.search(digit_pattern, string, re.IGNORECASE)
    else:
        match = re.search(digit_pattern2, string, re.IGNORECASE)
    
    if match:
        if match.group(0).isdigit():
            return match.group(0)
        else:
            if n==1:
                return str(digit_mapping[match.group(0).lower()])
            else:
                
                return str(digit_mapping[match.group(0)[::-1].lower()])
    else:
        return None
    
    

def main():
    filename = sys.argv[1]+".txt"
    sum_of_digits = 0

    with open(filename, "r") as file:
        lines = [line.rstrip("\n") for line in file]

    for string in lines:
        print(string)
        first_digit = find_digit_spelled_with_letters(string,1)
        print(first_digit)
        last_digit = find_digit_spelled_with_letters(string[::-1],2)
        print(last_digit)
        concat=first_digit+last_digit
        sum_of_digits += int(concat)

    print(sum_of_digits)



main()