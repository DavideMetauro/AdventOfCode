##### NON FUNZIONANTE #####

x=50
c=0
with open('input_day1.txt', 'r') as file:
    for line in file:
        op=line[0]
        y=int(line[1:].strip())

        if op=='L':
            y=-y

        c+= abs(abs(y)//100 + (x + y%100)//100)
        x=(x + y%100)%100
        
print(c)