lines = []
with open("input_day3.txt") as f:
    lines = f.readlines()

c=0
for line in lines:
    line = line.strip()
    max1 = max(line[:-1])
    idx = line.find(max1)
    max2 = max(line[idx+1:])
    c+=int(max1+max2)
print(c)