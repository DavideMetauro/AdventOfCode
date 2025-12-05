ranges=[]
with open("input_day5.txt") as file:
    for line in file:
        if line.strip() == "":
            break
        ranges.append(line.strip())
ranges=sorted(ranges, key=lambda x: int(x.split("-")[0]))  
#crea un set vuoto chiamato range_set
# parse ranges into list of (int_start, int_end)
intervals = []
for line in ranges:
    s, e = line.split("-")
    intervals.append((int(s), int(e)))

# sort by start
intervals.sort(key=lambda x: x[0])

# merge intervals into a new list
merged = []
for s, e in intervals:
    if not merged:
        merged.append([s, e])
    else:
        last_s, last_e = merged[-1]
        # if overlapping or contiguous, merge
        if s <= last_e +1 :
            new_s = last_s
            new_e = max(last_e, e)
            #print(f"Merging {last_s}-{last_e} and {s}-{e} into {new_s}-{new_e}")
            merged[-1][1] = new_e
        else:
            merged.append([s, e])

# convert merged intervals back to the original string format
ranges = [f"{s}-{e}" for s, e in merged]

# ranges=sorted(ranges, key=lambda x: int(x.split("-")[0]))  

count = 0
for range in ranges:
    start_range, end_range = range.split("-")
    count += int(end_range) - int(start_range) + 1

print(count)