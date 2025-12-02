#read input_day1.txt file one line at a time
x=50
c=0
with open('input_day1.txt', 'r') as file:
    for line in file:
        op=line[0]
        y=int(line[1:].strip())
        
        if op=='L':
            y=-y
        
        x=(x+y)%100
        
        c+= 1 if x==0 else 0

print(c)