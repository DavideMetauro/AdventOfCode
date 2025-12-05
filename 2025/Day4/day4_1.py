with open("input_day4.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

# iterate over lines as a matrix and if the element is a @, check if in the sourrounding 8 elements there is at least 4 @
count = 0
for i in range(0, len(lines) ):
    for j in range(0, len(lines[i]) ):
        if lines[i][j] == "@":
            at_count = 0
            # check the 8 surrounding elements
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (x == 0 and y == 0) or i + x < 0 or i + x >= len(lines) or j + y < 0 or j + y >= len(lines[i]):
                        continue
                    if lines[i + x][j + y] == "@":
                        at_count += 1
            if at_count < 4:
                count += 1
print(count)