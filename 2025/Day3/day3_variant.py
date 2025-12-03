def maxjolt(lines, n):
    c=0
    for line in lines:
        line = line.strip()
        idx = 0
        num = ''
        for i in range(n-1, -1, -1):
            sliced_line = line[idx:-i] if i!=0 else line[idx:]
            max_char = max(sliced_line)
            idx += sliced_line.find(max_char)+1
            num += max_char
        c+=int(num)
    return c

if __name__ == "__main__":
    lines = []
    with open("input_day3.txt") as f:
        lines = f.readlines()
    print("Part 1: ", maxjolt(lines, 2))
    print("Part 2: ", maxjolt(lines, 12))
