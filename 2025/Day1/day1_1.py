#read input_day1.txt file one line at a time
n=50
c=0
with open('input_day1.txt', 'r') as file:
    for line in file:
        op=line[0]
        num=int(line[1:].strip())
        if op=='L':
            n=(n-num)%100
        elif op=='R':
            n=(n+num)%100
        if n==0:
            c+=1
print(c)