with open("input_day6_transposed.txt") as file:
    lines = [line.strip() for line in file.readlines()]
#breakpoint()
numbers=[]
for l in lines:
    numbers.append(int(l) if l.isnumeric() else None)
    
with open("input_day6.txt") as file:
    operands = file.readlines()[-1].split()

# Calculate the result 
count=0
i=0
result=1
for n in numbers:
    if n == None:
        i+=1
        count += result
        result = 1
        print(count)
        continue
    op=operands[i]
    if op == '+':
        result=0
        count += n
    elif op == '*':
        result *= n
    
    
print(count)