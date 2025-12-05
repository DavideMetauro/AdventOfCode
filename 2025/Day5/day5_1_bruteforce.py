with open("input_day5.txt") as file:
    #read lines one by one till blank line, store them in a list called ranges, then read the rest of the file and store the lines in a list called ids
    ranges = []
    ids = []
    f = True
    for line in file:
        if line.strip() == "":
            f = False
            continue
        if f:
            ranges.append(line.strip())
        else:
            ids.append(line.strip())

import time
start_time = time.time()
# for each id in ids, check if it is in any of the ranges in ranges
count = 0
for id in ids:
    for r in ranges:
        r_split = r.split("-")
        if int(id) >= int(r_split[0]) and int(id) <= int(r_split[1]):
            count += 1
            break
print(count)
print("Execution time:", time.time() - start_time)