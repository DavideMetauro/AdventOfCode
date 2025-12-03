lines = []
with open("input_day3.txt") as f:
    lines = f.readlines()

c=0
for line in lines:
    line = line.strip()
    idx = 0
    num = ''
    for i in range(11, -1, -1):
        sliced_line = line[idx:-i] if i!=0 else line[idx:]
        print('i:', i)
        print('idx:', idx)
        print(line)
        print(sliced_line)
        max_char = max(sliced_line)
        idx += sliced_line.find(max_char)+1
        num += max_char
    c+=int(num)
print(c)