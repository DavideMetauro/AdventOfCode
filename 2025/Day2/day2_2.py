#read a line from input_day2.txt and split based on comma
with open('input_day2.txt', 'r') as file:
    line = file.readline().strip()
    ranges = line.split(',') 

c=0

for r in ranges:
    #split each range based on hyphen
    start, end = map(int, r.split('-'))
    for num in range(start, end + 1):
        s=str(num)
        for n in range(1, len(s)//2 + 1):
            if len(s)%n==0:
                chunks = [s[i:i+n] for i in range(0, len(s), n)]
                if all(chunk == chunks[0] for chunk in chunks):
                    c+=num
                    break

print(c)