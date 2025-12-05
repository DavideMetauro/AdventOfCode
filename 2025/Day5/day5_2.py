ranges=[]
with open("input_day5.txt") as file:
    for line in file:
        if line.strip() == "":
            break
        ranges.append(line.strip())
ranges=sorted(ranges, key=lambda x: int(x.split("-")[0]))  
new_ranges=set()
#crea un set vuoto chiamato range_set
for line in ranges:
    start_range, end_range = line.split("-")
    for line2 in ranges:
        if line == line2:
            continue
        f=False
        start_range2, end_range2 = line2.split("-")
        if int(start_range2) <= int(start_range) <= int(end_range2):
            start_range = start_range2
            f=True
        if int(end_range2) > int(end_range) >= int(start_range2):
            end_range = end_range2
            f=True
        if f:
            print(f"Merging {line} and {line2} into {start_range}-{end_range}")
            # ranges.remove(line2)
            # ranges.append(f"{start_range}-{end_range}")
    new_ranges.add(f"{start_range}-{end_range}")
    print(f"added: {start_range}-{end_range}")
            
new_ranges=sorted(new_ranges, key=lambda x: int(x.split("-")[0]))
print("Final ranges:")
for r in new_ranges:
    print(r)
#print(new_ranges)

# print("Merged ranges:")
# for i in range(len(start_list)):
#     print(f"{start_list[i]}-{end_list[i]}")
count = 0
for range in new_ranges:
    start_range, end_range = range.split("-")
    count += int(end_range) - int(start_range) + 1

print(count)