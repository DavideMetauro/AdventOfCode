#read a line from input_day2.txt and split based on comma
with open('input_day2.txt', 'r') as file:
    line = file.readline().strip()
    ranges = line.split(',') 

c=0
for r in ranges:
    #split each range based on hyphen
    start, end = map(int, r.split('-'))
    #print all numbers in the range
    for num in range(start, end + 1):
        s=str(num)
        if s[:len(s)//2]==s[len(s)//2:]:
            c+=num
print(c)